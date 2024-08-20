import datetime
from odoo import fields, api, models,_
import datetime
import babel
from collections import defaultdict
from datetime import date, datetime, time
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from pytz import timezone
from pytz import utc
from odoo.exceptions import UserError, ValidationError


class AccountJournalEntryReport(models.TransientModel):
    _name = "account.report.journal.entry"
    _description = "Journal entry filter"


    date_from = fields.Date(string='Date from', default=lambda self: fields.Date.to_string(
                              (datetime.now() + relativedelta(months=-1, day=1)).date()))
    date_to = fields.Date(string='Date to', default=lambda self: fields.Date.to_string(
                              (datetime.now() + relativedelta(months=0, day=1, days=-1)).date()))

    def print(self):

        if self.date_to < self.date_from:
            raise ValidationError(
                _("start Date must be less than end Date"))
        if self.date_from and self.date_to:
           acc = self.env['account.move'].search([('date', '>=', self.date_from), ('date', '<=', self.date_to)])
           if not acc:
               raise ValidationError(
                   _("There is no Journal entry in between selected Date"))
        elif self.date_from and not self.date_to:
            acc = self.env['account.move'].search([('date', '>=', self.date_from)])
        elif not self.date_from and self.date_to:
            acc = self.env['account.move'].search([('date', '<=', self.date_to)])
        else:
            acc = self.env['account.move'].search([])
        return self.env.ref('rsw_print_journal_entries.journal_entry_report_id').report_action(acc)

