import datetime
from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    create_product = fields.Boolean()

    @api.onchange('partner_id')
    def create_product_line(self):
        if self.partner_id and self.create_product:
            self.order_line = False
            date = datetime.date.today() - datetime.timedelta(days=14)
            sale_order = self.search([('create_date', '>=', date), ('partner_id', '=', self.partner_id.id)])
            product_list = []
            for order in sale_order:
                for line in order.order_line:
                    if line.product_id and line.product_id.id not in product_list:
                        product_list.append(line.product_id.id)
            sale_order_line = []
            if product_list:
                for product in product_list:
                    product_id = self.order_line.product_id.browse(product)
                    sale_order_line.append(
                        (0, 0,
                         {'product_id': product, 'product_uom_qty': 0.0, 'price_unit': product_id.lst_price,
                          'name': product_id.get_product_multiline_description_sale(),
                          'product_uom': product_id.uom_id.id}))
            if sale_order_line:
                self.order_line = sale_order_line

    def action_confirm(self):
        for line in self.order_line:
            if line.product_uom_qty <= 0:
                line.unlink()
        data = super(SaleOrder, self).action_confirm()
        return data
