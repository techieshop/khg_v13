

from odoo import api, models
from odoo.exceptions import UserError


class ExtendTrialBalance(models.AbstractModel):
    _inherit = 'report.accounting_pdf_reports.report_trialbalance'
    _description = 'Report Trial Balance customized'

    @api.model
    def create(self, vals):
        res = super(ExtendTrialBalance,self).create(vals)
        return res


    @api.model
    def _get_report_values(self, docids, data=None):
        res = super(ExtendTrialBalance, self)._get_report_values(docids,data)
        accs = res['Accounts']
        fixed_asset = []
        fixed_total = {
            'debit' : 0,
            'credit' : 0,
            'balance' : 0
        }
        liability = []
        liability_total = {
            'debit' : 0,
            'credit' : 0,
            'balance' : 0
        }
        current_asset = []
        current_total = {
            'debit' : 0,
            'credit' : 0,
            'balance' : 0
        }
        capital = []
        capital_total = {
            'debit' : 0,
            'credit' : 0,
            'balance' : 0
        }
        others = []
        total_all = {
            'debit': 0,
            'credit': 0,
            'balance': 0
        }

        for acc in accs :
            code = acc['code']
            total_all['debit'] +=acc['debit']
            total_all['credit'] += acc['credit']
            total_all['balance'] += acc['balance']
            first_code = code[:2]
            first_code = int(first_code)
            if 10 <= first_code <= 14:
                fixed_asset.append(acc)
                fixed_total['debit'] += acc['debit']
                fixed_total['credit'] += acc['credit']
                fixed_total['balance'] += acc['balance']
            elif 15<= first_code <= 19 :
                current_asset.append(acc)
                current_total['debit'] += acc['debit']
                current_total['credit'] += acc['credit']
                current_total['balance'] += acc['balance']
            elif first_code == 20 :
                liability.append(acc)
                liability_total['debit'] += acc['debit']
                liability_total['credit'] += acc['credit']
                liability_total['balance'] += acc['balance']
            elif 30 <= first_code <= 39:
                capital.append(acc)
                capital_total['debit'] += acc['debit']
                capital_total['credit'] += acc['credit']
                capital_total['balance'] += acc['balance']
            else:
                others.append(acc)
        print(liability)
        print(fixed_asset)
        print(current_asset)
        print(capital)
        print(others)
        res['fixed_assets'] = fixed_asset
        res['fixed_total'] = fixed_total
        res['current_assets'] = current_asset
        res['current_total'] = current_total
        res['liability'] = liability
        res['liability_total'] = liability_total
        res['capital'] = capital
        res['capital_total'] = capital_total
        res['others'] = others
        res['total_all'] = total_all
        return res
