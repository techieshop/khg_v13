# -*- coding: utf-8 -*-

import time
from odoo import api, models, _
from odoo.exceptions import UserError


class ReportTrialBalance(models.AbstractModel):
    _inherit = 'report.accounting_pdf_reports.report_trialbalance'

    @api.model
    def _get_report_values(self, docids, data=None):
        res = super(ReportTrialBalance, self)._get_report_values(docids, data)
        total_line = {}
        total_credit = 0.0
        total_debit = 0.0
        total_balance = 0.0
        if 'Accounts' in res:
            for data in res.get('Accounts'):
                total_credit += ((data["credit"]) if data.get('credit') else 0.0)
                total_debit += ((data["debit"]) if data.get('debit') else 0.0)
                total_balance += ((data["balance"]) if data.get('balance') else 0.0)
        total_line['total_credit'] = total_credit
        total_line['total_debit'] = total_debit
        total_line['total_balance'] = total_balance
        res['total_line'] = total_line
        return res
