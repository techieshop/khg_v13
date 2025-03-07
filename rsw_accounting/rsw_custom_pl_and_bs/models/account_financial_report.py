from odoo import api, fields, models


class AccountFinancialReport(models.Model):
    _inherit = "account.financial.report"

    root_parent_id = fields.Many2one("account.financial.report", compute="_compute_root_parent_id", store=True)
    sequence = fields.Integer(default=10)
    number_of_blank_lines = fields.Integer(default=0)
    style_overwrite = fields.Selection(
        selection_add=[
            ('7', 'Normal Text + Single Top Line'),
            ('8', 'Normal Text + Single Top Line + Double Under Line'),
        ]
    )

    @api.depends("parent_id", "parent_id.root_parent_id")
    def _compute_root_parent_id(self):
        for record in self:
            parent_id = record.parent_id
            record.root_parent_id = parent_id
            while parent_id:
                record.root_parent_id = parent_id
                parent_id = parent_id.parent_id
