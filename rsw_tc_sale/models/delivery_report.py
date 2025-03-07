from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def print_delivery_report(self):
        return self.env.ref('rsw_tc_sale.report_shipment_card').report_action(self)

    def get_sale_order_line(self):
        data = {}
        for line in self.sale_order_line_ids:
            if line.product_id.name in data:
                data.get(line.product_id.name)['product_uom_qty'] += line.product_uom_qty
                data.get(line.product_id.name)['qty_delivered'] += line.qty_delivered
                data.get(line.product_id.name)['qty_invoiced'] += line.qty_invoiced
                data.get(line.product_id.name)['qty_to_invoice'] += line.qty_to_invoice
                data.get(line.product_id.name)['price_subtotal'] += line.price_subtotal
            else:
                data[line.product_id.name] = {'product_uom_qty': line.product_uom_qty,
                                              'qty_delivered': line.qty_delivered,
                                              'qty_invoiced': line.qty_invoiced,
                                              'qty_to_invoice': line.qty_to_invoice,
                                              'price_subtotal': line.price_subtotal}
        return data
