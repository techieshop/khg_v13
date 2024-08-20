from email.policy import default
from odoo import api, fields, models, _
import time

class AccountingReport(models.TransientModel):
    _inherit = 'accounting.report'

    date_from = fields.Date(string='Start Date', default = time.strftime('2020-04-01'), store=True)
    # date_from = fields.Date(string='Start Date', default=time.strftime('2021-04-01'), store=True)
    # date_from = fields.Date(string='Start Date', default = time.strftime('%Y-04-01'), store=True)

    date_to = fields.Date(string='End Date', default = time.strftime('2021-03-31'),store=True)
    # date_to = fields.Date(string='End Date', default = time.strftime('2022-03-31'),store=True)
    # date_to = fields.Date(string='End Date',compute='_compute_end_date',inverse='_inverse_end_date',store=True)

    enable_filter = fields.Boolean(string='Enable Comparison', default=True, store=True)
    # comparison
    label_filter = fields.Char(string='Column Label', default='至上期')
    filter_cmp = fields.Selection([('filter_no', 'No Filters'), ('filter_date', 'Date')],string='Filter by',default='filter_date',store=True)
    # date_from_cmp=fields.Date(string='From Date',compute='_compute_from_date',inverse='_inverse_from_date',store=True)
    # date_to_cmp= fields.Date(string='To Date',compute='_compute_to_date',inverse='_inverse_to_date',store=True)
    # date_from_cmp=fields.Date(string='From Date', default = time.strftime('2020-04-01'),store=True)
    # date_to_cmp= fields.Date(string='To Date',default = time.strftime('2021-03-31') ,store=True)
    #
    @api.depends('date_from')
    def _compute_end_date(self):
        year = int(self.date_from.strftime('%Y'))

        self.date_to = time.strftime('%s-03-31' %(year+1))


    def _inverse_end_date(self):
        self.date_to = time.strftime('%Y-03-31' )

    @api.depends('date_from')
    def _compute_to_date(self):
        year = int(self.date_from.strftime('%Y'))

        self.date_to_cmp = time.strftime('%s-03-31' %(year))

    def _inverse_to_date(self):
        self.date_to_cmp = time.strftime('%Y-03-31' )

    @api.depends('date_from')
    def _compute_from_date(self):
        year = int(self.date_from.strftime('%Y'))

        self.date_from_cmp = time.strftime('%s-04-01' %(year-1))

    def _inverse_from_date(self):
        self.date_to_cmp = time.strftime('%Y-04-01' )