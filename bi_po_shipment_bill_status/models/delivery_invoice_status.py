# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from odoo.tools.float_utils import float_compare

class inherit_purchase(models.Model):
	_inherit = "purchase.order"
	
	check_partially_delivery = fields.Boolean(string="Partially Shipped",readonly=1,copy=False)
	check_fully_delivery = fields.Boolean(string="Fully Shipped",readonly=1,copy=False)
	check_partially_paid = fields.Boolean(string="Partially Paid",readonly=1,copy=False)
	check_fully_paid = fields.Boolean(string="Fully Paid",default=False,readonly=1,copy=False)



class inherit_stock_picking(models.Model):
	_inherit = "stock.picking"

	pick_bool = fields.Boolean(string="demo bool",compute="_compute_purchase_fully_picking",store=True)

	@api.depends("move_ids_without_package.quantity_done")
	def _compute_purchase_fully_picking(self):
		
		for i in self:
			purchase_order = i.env['purchase.order'].search([])
			for j in purchase_order:
				if j.name == i.origin:
					counter_qty = 0.0
					main_qty = 0.0

					for ids in j.picking_ids:
						for lines in ids.move_ids_without_package:
							counter_qty += lines.quantity_done

					for main in j.order_line:
						main_qty += main.product_qty

					if counter_qty > 0.0:

						if counter_qty < main_qty:
							j.write({
								"check_partially_delivery":True
									})

						if counter_qty == main_qty:
							j.write({
								"check_fully_delivery":True,
								"check_partially_delivery":False
									})

					i.pick_bool = True


class inherit_invoicing(models.Model):
	_inherit = "account.move"

	def _compute_amount(self):
		invoice_ids = [move.id for move in self if move.id and move.is_invoice(include_receipts=True)]
		self.env['account.payment'].flush(['state'])
		if invoice_ids:
			self._cr.execute(
				'''
                    SELECT move.id
                    FROM account_move move
                    JOIN account_move_line line ON line.move_id = move.id
                    JOIN account_partial_reconcile part ON part.debit_move_id = line.id OR part.credit_move_id = line.id
                    JOIN account_move_line rec_line ON
                        (rec_line.id = part.credit_move_id AND line.id = part.debit_move_id)
                        OR
                        (rec_line.id = part.debit_move_id AND line.id = part.credit_move_id)
                    JOIN account_payment payment ON payment.id = rec_line.payment_id
                    JOIN account_journal journal ON journal.id = rec_line.journal_id
                    WHERE payment.state IN ('posted', 'sent')
                    AND journal.post_at = 'bank_rec'
                    AND move.id IN %s
                ''', [tuple(invoice_ids)]
			)
			in_payment_set = set(res[0] for res in self._cr.fetchall())
		else:
			in_payment_set = {}

		for move in self:
			total_untaxed = 0.0
			total_untaxed_currency = 0.0
			total_tax = 0.0
			total_tax_currency = 0.0
			total_residual = 0.0
			total_residual_currency = 0.0
			total = 0.0
			total_currency = 0.0
			currencies = set()

			for line in move.line_ids:
				if line.currency_id:
					currencies.add(line.currency_id)

				if move.is_invoice(include_receipts=True):
					# === Invoices ===

					if not line.exclude_from_invoice_tab:
						# Untaxed amount.
						total_untaxed += line.balance
						total_untaxed_currency += line.amount_currency
						total += line.balance
						total_currency += line.amount_currency
					elif line.tax_line_id:
						# Tax amount.
						total_tax += line.balance
						total_tax_currency += line.amount_currency
						total += line.balance
						total_currency += line.amount_currency
					elif line.account_id.user_type_id.type in ('receivable', 'payable'):
						# Residual amount.
						total_residual += line.amount_residual
						total_residual_currency += line.amount_residual_currency
				else:
					# === Miscellaneous journal entry ===
					if line.debit:
						total += line.balance
						total_currency += line.amount_currency

			if move.type == 'entry' or move.is_outbound():
				sign = 1
			else:
				sign = -1
			move.amount_untaxed = sign * (total_untaxed_currency if len(currencies) == 1 else total_untaxed)
			move.amount_tax = sign * (total_tax_currency if len(currencies) == 1 else total_tax)
			move.amount_total = sign * (total_currency if len(currencies) == 1 else total)
			move.amount_residual = -sign * (total_residual_currency if len(currencies) == 1 else total_residual)
			move.amount_untaxed_signed = -total_untaxed
			move.amount_tax_signed = -total_tax
			move.amount_total_signed = abs(total) if move.type == 'entry' else -total
			move.amount_residual_signed = total_residual

			currency = len(currencies) == 1 and currencies.pop() or move.company_id.currency_id
			is_paid = currency and currency.is_zero(move.amount_residual) or not move.amount_residual

			# Compute 'invoice_payment_state'.
			if move.type == 'entry':
				move.invoice_payment_state = False
			elif move.state == 'posted' and is_paid:
				if move.id in in_payment_set:
					move.invoice_payment_state = 'in_payment'

				else:
					move.invoice_payment_state = 'paid'
					move.purchase_id.write({
						"check_partially_paid": False,
						"check_fully_paid": True
					})
			else:
				move.invoice_payment_state = 'not_paid'
				move.purchase_id.write({
					"check_partially_paid": True,

				})
		res = super(inherit_invoicing, self)._compute_amount()
		return  res






