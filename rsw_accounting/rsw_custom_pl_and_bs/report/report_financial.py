from odoo import _, api, fields, models, tools


class ReportFinancial(models.AbstractModel):
    _inherit = 'report.accounting_pdf_reports.report_financial'

    def get_account_lines(self, data):
        # Override some part of the function
        lines = []
        account_report = self.env['account.financial.report'].search([('id', '=', data['account_report_id'][0])])
        pl_account_report = self.env.ref("accounting_pdf_reports.account_financial_report_profitandloss0")
        bs_account_report = self.env.ref("accounting_pdf_reports.account_financial_report_balancesheet0")
        is_bs_report = data.get("account_report_id", [0])[0] == bs_account_report.id
        child_reports = account_report._get_children_by_order()
        res = self.with_context(data.get('used_context'))._compute_report_balance(child_reports)
        if data['enable_filter']:
            comparison_res = self.with_context(data.get('comparison_context'))._compute_report_balance(child_reports)
            for report_id, value in comparison_res.items():
                res[report_id]['comp_bal'] = value['balance']
                report_acc = res[report_id].get('account')
                if report_acc:
                    for account_id, val in comparison_res[report_id].get('account').items():
                        report_acc[account_id]['comp_bal'] = val['balance']
        for report in child_reports:
            vals = {
                'name': report.name,
                'balance': res[report.id]['balance'] * float(report.sign),  # OVERRIDE Add float on report.sign
                'type': 'report',
                'level': bool(report.style_overwrite) and report.style_overwrite or report.level,
                'account_type': report.type or False,  # used to underline the financial report balances
                "display_detail": report.display_detail,  # OVERRIDE add new key
            }
            if data['debit_credit']:
                vals['debit'] = res[report.id]['debit']
                vals['credit'] = res[report.id]['credit']

            if data['enable_filter']:
                vals['balance_cmp'] = res[report.id]['comp_bal'] * float(report.sign)  # OVERRIDE Add float on report.sign

            lines.append(vals)
            if report.display_detail == 'no_detail':
                # the rest of the loop is used to display the details of the financial report, so it's not needed here.
                # OVERRIDE add blank lines based on configurator
                if report.number_of_blank_lines:
                    lines += [
                        {
                            "account_type": "other",
                            "balance": 0,
                            "balance_cmp": 0,
                            "credit": 0,
                            "debit": 0,
                            "level": 0,
                            "name": "",
                            "type": "blank",
                        } for i in range(report.number_of_blank_lines)
                    ]
                continue
            origin_vals = vals
            if res[report.id].get('account'):
                sub_lines = []
                for account_id, value in res[report.id]['account'].items():
                    # if there are accounts to display, we add them to the lines with a level equals to their level in
                    # the COA + 1 (to avoid having them with a too low level that would conflicts with the level of data
                    # financial reports for Assets, liabilities...)
                    flag = False
                    account = self.env['account.account'].browse(account_id)
                    vals = {
                        'name': account.code + ' ' + account.name,
                        'balance': value['balance'] * float(report.sign) or 0.0,  # OVERRIDE Add float on report.sign
                        'type': 'account',
                        'level': report.display_detail == 'detail_with_hierarchy' and 4,
                        'account_type': account.internal_type,
                        "display_detail": "",  # OVERRIDE add new key
                    }
                    if data['debit_credit']:
                        vals['debit'] = value['debit']
                        vals['credit'] = value['credit']
                        if not account.company_id.currency_id.is_zero(vals['debit']) or not account.company_id.currency_id.is_zero(vals['credit']):
                            flag = True
                    if not account.company_id.currency_id.is_zero(vals['balance']):
                        flag = True
                    if data['enable_filter']:
                        vals['balance_cmp'] = value['comp_bal'] * float(report.sign)  # OVERRIDE Add float on report.sign
                        if not account.company_id.currency_id.is_zero(vals['balance_cmp']):
                            flag = True
                    if flag:
                        sub_lines.append(vals)
                lines += sorted(sub_lines, key=lambda sub_line: sub_line['name'])
                # OVERRIDE add total line
                # if is_bs_report:
                #     lines += [
                #         {
                #             "account_type": "other",
                #             "balance": origin_vals.get("balance", 0),
                #             "balance_cmp": origin_vals.get("balance_cmp", 0),
                #             "credit": origin_vals.get("credit", 0),
                #             "debit": origin_vals.get("debit", 0),
                #             "level": 4,
                #             "name": _("Subtotal"),
                #             "type": "subtotal"
                #         },
                #         {
                #             "account_type": "other",
                #             "balance_cmp": 0,
                #             "balance": 0,
                #             "credit": 0,
                #             "debit": 0,
                #             "level": 0,
                #             "name": "",
                #             "type": "blank",
                #         },
                #     ]
            # OVERRIDE add blank lines based on configurator
            if report.number_of_blank_lines:
                lines += [
                    {
                        "account_type": "other",
                        "balance": 0,
                        "balance_cmp": 0,
                        "credit": 0,
                        "debit": 0,
                        "level": 0,
                        "name": "",
                        "type": "blank",
                    } for i in range(report.number_of_blank_lines)
                ]
        # OVERRIDE add customize for pl, bs report
        if lines:
            if data.get("account_report_id", [0])[0] == pl_account_report.id:
                lines = self.customize_pl_report(lines)
            elif data.get("account_report_id", [0])[0] == bs_account_report.id:
                lines = self.customize_bs_report(lines)
        return lines

    def _compute_report_balance(self, reports):
        '''returns a dictionary with key=the ID of a record and value=the credit, debit and balance amount
           computed for this record. If the record is of type :
               'accounts' : it's the sum of the linked accounts
               'account_type' : it's the sum of leaf accoutns with such an account_type
               'account_report' : it's the amount of the related report
               'sum' : it's the sum of the children of this record (aka a 'view' record)'''
        res = {}
        fields = ['credit', 'debit', 'balance']
        for report in reports:
            if report.id in res or (
                self.env.context.get("filter_subtotal")
                and report.display_detail == "no_detail"
                and report.type not in ["sum", "account_report"]
            ):
                continue
            res[report.id] = dict((fn, 0.0) for fn in fields)
            if report.type == 'accounts':
                # it's the sum of the linked accounts
                res[report.id]['account'] = self._compute_account_balance(report.account_ids)
                for value in res[report.id]['account'].values():
                    for field in fields:
                        res[report.id][field] += value.get(field)
            elif report.type == 'account_type':
                # it's the sum the leaf accounts with such an account type
                accounts = self.env['account.account'].search([('user_type_id', 'in', report.account_type_ids.ids)])
                res[report.id]['account'] = self._compute_account_balance(accounts)
                for value in res[report.id]['account'].values():
                    for field in fields:
                        res[report.id][field] += value.get(field)
            elif report.type == 'account_report' and report.account_report_id:
                # it's the amount of the linked report
                res2 = self._compute_report_balance(report.account_report_id)
                for key, value in res2.items():
                    for field in fields:
                        res[report.id][field] += value[field]
            elif report.type == 'sum':
                # it's the sum of the children of this account.report
                res2 = self.with_context(filter_subtotal=True)._compute_report_balance(report.children_ids)
                for key, value in res2.items():
                    for field in fields:
                        res[report.id][field] += value[field]
        return res

    def customize_pl_report(self, lines):
        # move first item to the last
        lines = lines[1:] + [lines[0]]
        # Add subtotal
        subtotal_dict = {}
        empty_subtotal = {
            "account_type": "other",
            "balance": 0,
            "balance_cmp": 0,
            "credit": 0,
            "debit": 0,
            "level": 4,
            "name": _("Subtotal"),
            "type": "subtotal"
        }
        blank_line = {
            "account_type": "other",
            "balance_cmp": 0,
            "balance": 0,
            "credit": 0,
            "debit": 0,
            "level": 0,
            "name": "",
            "type": "blank",
        }
        for line in lines:
            if not line.get("type", "") == "account":
                continue
            account_prefix = line.get("name")[0]
            if account_prefix not in subtotal_dict:
                subtotal_dict[account_prefix] = {**empty_subtotal}
            subtotal_dict[account_prefix]["balance"] += line.get("balance", 0)
            subtotal_dict[account_prefix]["balance_cmp"] += line.get("balance_cmp", 0)
            subtotal_dict[account_prefix]["credit"] += line.get("credit", 0)
            subtotal_dict[account_prefix]["debit"] += line.get("debit", 0)
        new_lines = []
        for line in lines:
            if (
                new_lines
                and new_lines[-1].get("type") == line.get("type") == "report"
                and new_lines[-1].get("account_type") not in ["account_report", "sum"]
            ):
                # new_lines.append(empty_subtotal)
                # new_lines.append(blank_line)
                new_lines.append(line)
                continue
            elif (
                not new_lines
                or new_lines[-1].get("type") in ["report", "blank"]
                or new_lines[-1].get("account_type") in ["account_report", "sum"]
            ):
                new_lines.append(line)
                continue
            elif not line.get("name"):
                new_lines.append(line)
                continue
            last_line = new_lines[-1]
            last_account_prefix = last_line.get("name")[0]
            current_account_prefix = line.get("name")[0]
            if line.get("type") == "report" or current_account_prefix != last_account_prefix:
                last_line = new_lines[-1]
                last_account_prefix = last_line.get("name")[0]
                # new_lines.append(subtotal_dict.get(last_account_prefix))
                # new_lines.append(blank_line)
                new_lines.append(line)
            else:
                new_lines.append(line)
        if new_lines:
            lines = new_lines
        # Hide the amount of the heading
        for line in lines:
            if (
                line["type"] == "report"
                and line != lines[-1]
                and line['display_detail'] != "no_detail"
                and line['account_type'] not in ["account_report", "sum"]
            ):
                line["is_hide_amount"] = True
        return lines

    def customize_bs_report(self, lines):
        # move first item to the last
        lines = lines[1:] + [lines[0]]
        # Hide the amount of the heading
        for line in lines:
            if (
                line["type"] == "report"
                and line != lines[-1]
                and line['display_detail'] != "no_detail"
                and line['account_type'] not in ["account_report", "sum"]
            ):
                line["is_hide_amount"] = True
        return lines

    def format_financial_amount(self, amount):
        if amount < 0:
            return "(" + tools.format_amount(self.env, abs(amount), self.env.company.currency_id) + ")"
        return tools.format_amount(self.env, amount, self.env.company.currency_id)

    def update_level(self, line):
        if int(line.get("level", 0)) in [7, 8]:
            line["level"] = 4
        return line

    @api.model
    def _get_report_values(self, docids, data=None):
        res = super(ReportFinancial, self)._get_report_values(docids, data=data)
        if "data" in res and res["data"].get("fiscal_year"):
            fiscal_year = res["data"]["fiscal_year"]
            res["fiscal_year_display"] = f"{int(fiscal_year) - 1} - {fiscal_year}"
        else:
            res["fiscal_year_display"] = ""
        res["format_financial_amount"] = self.format_financial_amount
        res["update_level"] = self.update_level
        return res
