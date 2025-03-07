# -*- coding: utf-8 -*-

from odoo import models, fields, api



class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    converted_total = fields.Float(compute='_compute_converted_total', string='Converted Total')
    sale_profit = fields.Float(compute='_compute_converted_total', string='Sale Profit')
    sale_margin = fields.Float(compute='_compute_converted_total', string='Sale Margin')
    second_currency = fields.Many2one('res.currency', string='Second Currency', required=True, help="Currency of your Company.", default=lambda self: self.env.user.company_id.currency_id.id)

    
    @api.depends('sale_order_id','amount_total')
    def _compute_converted_total(self):
        currency=self.env['res.currency'].search([('name','=','HKD')],limit=1)
        for rec in self:
                converted_total=round(( rec.amount_total / rec.currency_id.rate) * currency.rate,2)
                rec.converted_total=converted_total
                if rec.sale_order_id:
                    rec.sale_profit=round(rec.sale_order_id.amount_total - converted_total,2)
                    rec.sale_margin=round((rec.sale_order_id.amount_total - converted_total )/ converted_total,2)
                else:
                    rec.sale_profit=0
                    rec.sale_margin=0
                if rec.second_currency != currency.id:
                    rec.second_currency=currency.id