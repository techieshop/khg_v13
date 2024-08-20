from odoo import fields, models,api


class StockMove(models.Model):
    _inherit = "stock.move"
    x_cartoon_in_stock = fields.Integer(compute='_compute_carton_weight',string="No. of Cartoon (Est)",default=1,store=True)
    x_product_standard_weight = fields.Float(compute='_compute_carton_weight',string="Packing Spec (kg/pack)",default=10.8,store=True,digits = (12,4))
    
    @api.depends('purchase_line_id','sale_line_id')
    def _compute_carton_weight(self):
        for record in self:
            if record.purchase_line_id:
                record.x_cartoon_in_stock=record.purchase_line_id.x_po_cartoon
                record.x_product_standard_weight=record.purchase_line_id.x_product_standard_weight
            elif record.sale_line_id:
                record.x_cartoon_in_stock=record.sale_line_id.x_so_cartoon
                record.x_product_standard_weight=record.sale_line_id.x_product_standard_weight
            else:
                record.x_cartoon_in_stock=record.x_cartoon_in_stock
                record.x_product_standard_weight=record.x_product_standard_weight

class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values):
        res = super(StockRule, self)._get_stock_move_values(product_id, product_qty, product_uom, location_id, name, origin, company_id, values)
        res['x_cartoon_in_stock'] = values.get('x_cartoon_in_stock')
        return res
    
# class StcokPicking(models.Model):
#     _inherit = "stock.picking"
#     x_cartoon_picked = fields.Integer(string="Cartoon")
