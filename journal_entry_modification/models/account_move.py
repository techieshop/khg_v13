# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountMoveInherit(models.Model):
    _inherit = "account.move"

    journal_number = fields.Char(store=True, string='Journal Number')
    voucher_number = fields.Char(store=True, string='Voucher Number')
    remarks = fields.Char(store=True, string='Remarks')
    status = fields.Char(store=True, string='Status')
    journal_type = fields.Char(store=True, string='Journal Type')
    description = fields.Text(store=True, string='Description')
    ar_type = fields.Char(store=True, string='AR Type')
    invoice_number = fields.Char(store=True, string='Invoice Number')
    created_by = fields.Many2one('res.users', String='Created By')
