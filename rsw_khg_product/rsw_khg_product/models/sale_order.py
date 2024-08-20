from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    x_product_standard_weight = fields.Float(string="Packing Spec (kg/pack)",default=10.8,digits = (12,4))
    x_so_cartoon = fields.Integer(string="No. of Cartoon",default=1)

    def _prepare_procurement_values(self, group_id=False):
        res = super(SaleOrderLine, self)._prepare_procurement_values(group_id)
        res['x_so_cartoon'] = self.x_so_cartoon
        return res

# class ProductTemplate(models.Model):
#     _inherit = "product.template"

#     x_cartoon = fields.Integer(string="No. of Cartoon")
    @api.onchange('x_product_standard_weight', 'x_so_cartoon')
    def onchange_cartoon(self):
        if self.x_product_standard_weight and self.x_so_cartoon:
            self.product_uom_qty = self.x_product_standard_weight * self.x_so_cartoon

# class SaleOrderLineTransient(models.TransientModel):
#     _inherit = "create.saleorder"
    
#     x_so_cartoon = fields.Integer(string="Cartoon", default=1)