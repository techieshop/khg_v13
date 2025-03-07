from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import ValidationError


class SoldProductReportWizard(models.TransientModel):
    _name = 'sold.product.report.wizard'
    _description = 'Sold Qty wizard.'

    delivery_date = fields.Date(string="Delivery Date", default= date.today())

    @api.constrains('delivery_date')
    def _check_date(self):
        if self.delivery_date > date.today():
            raise ValidationError(_('Please Select Valid Date'))

    def print_product_report(self):
        self.ensure_one()
        data = {
            'date' : self.delivery_date
        }
        return self.env.ref('sold_product_qty_report.action_report_sold_saleorder').report_action(None, data=data)

