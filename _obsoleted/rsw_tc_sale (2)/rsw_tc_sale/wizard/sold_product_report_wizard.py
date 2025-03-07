from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import ValidationError


class SoldProductReportWizard(models.TransientModel):
    _name = 'sold.product.report.wizard'
    _description = 'Sold Qty wizard.'

    delivery_date = fields.Date(string="Delivery Date", default= date.today())
    start_date = fields.Date(string="Start Date", default= date.today())
    end_date = fields.Date(string="End Date", default= date.today())


    @api.constrains('from_date', 'to_date')
    def _check_dates(self):
        if self.to_date > self.from_date:
            raise ValidationError(_(''))


    @api.constrains('delivery_date')
    def _check_date(self):
        if self.delivery_date > date.today():
            raise ValidationError(_('End Date must be greater than Start Date.'))

    def print_product_report(self):
        self.ensure_one()
        data = {
            'date' : self.delivery_date,
            'contex' : self.env.context,
            'start_date' : self.start_date,
            'end_date' : self.end_date
        }
        return self.env.ref('rsw_tc_sale_reports.action_report_sold_saleorder').report_action(None, data=data)

