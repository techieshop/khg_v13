from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = 'account.move'

    def _print_report(self):
        print('oo')
        # return self.env.ref('rsw_print_journal_entries.journal_entry_report_id').report_action(self)