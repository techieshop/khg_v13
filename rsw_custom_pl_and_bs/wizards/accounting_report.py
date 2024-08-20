import datetime
from dateutil.relativedelta import relativedelta

from odoo import _, api, exceptions, fields, models
from odoo.tools.misc import format_date


class AccountingReport(models.TransientModel):
    _inherit = "accounting.report"

    @api.model
    def _get_fiscal_year(self):
        current_year = fields.Date.today().year
        result = []
        for i in range(2020, current_year + 2):
            result.append((str(i), f"{str(i - 1)} - {str(i)}"))
        return result

    @api.model
    def _get_fiscal_month(self):
        return [
            ("01", "01"),
            ("02", "02"),
            ("03", "03"),
            ("04", "04"),
            ("05", "05"),
            ("06", "06"),
            ("07", "07"),
            ("08", "08"),
            ("09", "09"),
            ("10", "10"),
            ("11", "11"),
            ("12", "12"),
        ]

    @api.model
    def _default_fiscal_year(self):
        return str(fields.Date.today().year)

    @api.model
    def _default_fiscal_month(self):
        return str(fields.Date.today().month).zfill(2)

    def _default_fiscal_month_start(self):
        return "04"

    def _default_fiscal_month_end(self):
        return "03"
    
    fiscal_year = fields.Selection("_get_fiscal_year", default=_default_fiscal_year)
    fiscal_month_start = fields.Selection("_get_fiscal_month", default=_default_fiscal_month_start)
    fiscal_month_end = fields.Selection("_get_fiscal_month", default=_default_fiscal_month_end)
    is_pl_report = fields.Boolean(compute="_compute_is_pl_report")
    is_pl_invalid_comparison = fields.Boolean(compute="_compute_is_pl_invalid_comparison")
    is_bs_report = fields.Boolean(compute="_compute_is_bs_report")

    @api.depends("account_report_id")
    def _compute_is_pl_report(self):
        pl_report = self.env.ref("accounting_pdf_reports.account_financial_report_profitandloss0")
        for record in self:
            record.is_pl_report = record.account_report_id == pl_report

    @api.depends("is_pl_report", "date_from", "enable_filter")
    def _compute_is_pl_invalid_comparison(self):
        for record in self:
            is_pl_invalid_comparison = False
            if record.enable_filter and record.is_pl_report and record.date_from:
                if record.date_from == datetime.date(self.date_from.year, 4, 1):
                    is_pl_invalid_comparison = True
            record.is_pl_invalid_comparison = is_pl_invalid_comparison

    @api.depends("account_report_id")
    def _compute_is_bs_report(self):
        bs_report = self.env.ref("accounting_pdf_reports.account_financial_report_balancesheet0")
        for record in self:
            record.is_bs_report = record.account_report_id == bs_report

    @api.constrains("date_from", "date_to")
    def _check_date_from_to(self):
        for record in self:
            if record.date_from > record.date_to:
                raise exceptions.ValidationError(
                    _("Start Date (%s) must be less than End Date (%s)")
                    % (format_date(self.env, record.date_from), format_date(self.env, record.date_to))
                )

    @api.onchange("fiscal_year", "fiscal_month_start", "fiscal_month_end")
    def _onchange_fiscal_date_part(self):
        # before_fiscal_month = [4, 5, 6, 7, 8, 9, 10, 11, 12]
        after_fiscal_month = [1, 2, 3]
        if self.fiscal_year:
            after_fiscal_year = int(self.fiscal_year)
            before_fiscal_year = int(self.fiscal_year) - 1

            if self.fiscal_month_start:
                fiscal_month_start = int(self.fiscal_month_start)
                fiscal_year_start = after_fiscal_year if fiscal_month_start in after_fiscal_month else before_fiscal_year
                self.date_from = datetime.date(fiscal_year_start, fiscal_month_start, 1)

            if self.fiscal_month_end:
                fiscal_month_end = int(self.fiscal_month_end)
                fiscal_year_end = after_fiscal_year if fiscal_month_end in after_fiscal_month else before_fiscal_year
                self.date_to = datetime.date(fiscal_year_end, fiscal_month_end, 1) + relativedelta(days=-1, months=1)

    @api.onchange("enable_filter", "date_from", "account_report_id", "date_to")
    def _onchange_enable_filter(self):
        if self.enable_filter and self.account_report_id:
            self.debit_credit = False
            self.filter_cmp = "filter_date"
            if self.date_from:
                after_fiscal_month = [1, 2, 3]
                fiscal_year = self.date_from.year - 1 if self.date_from.month in after_fiscal_month else self.date_from.year
                if self.date_from == datetime.date(self.date_from.year, 4, 1):
                    if self.is_pl_report:
                        # For PL Report, the comparison column must be all zero
                        self.date_to_cmp = self.date_from
                        self.date_from_cmp = self.date_to
                    elif self.is_bs_report:
                        # For BS Report, the comparison column will be the first fiscal month
                        self.date_from_cmp = datetime.date(2018, 4, 1)
                        # self.date_to_cmp = datetime.date(fiscal_year, 3, 31)
                        self.date_to_cmp = self.date_from + relativedelta(days=-1)
                else:
                    self.date_to_cmp = self.date_from + relativedelta(days=-1)
                    if self.is_pl_report:
                        self.date_from_cmp = datetime.date(fiscal_year, 4, 1)
                    elif self.is_bs_report:
                        self.date_from_cmp = datetime.date(2018, 4, 1)

    def check_report(self):
        res = super(AccountingReport, self).check_report()
        res['data']['form']['fiscal_year'] = self.fiscal_year
        res['data']['form']['fiscal_month_start'] = self.fiscal_month_start
        res['data']['form']['fiscal_month_end'] = self.fiscal_month_end
        return res
