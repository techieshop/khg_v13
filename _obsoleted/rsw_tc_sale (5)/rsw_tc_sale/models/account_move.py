from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    voucher_no = fields.Char("Voucher No")
    description = fields.Text("Description")
    account_no = fields.Integer("Account")
    debit_amount = fields.Float("Debit")
    credit_amount = fields.Float("Credit")
    invoice_no = fields.Integer("Invoice No")