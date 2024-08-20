from odoo import fields, models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"
    x_cartoon_in_stock = fields.Integer(related='move_id.x_cartoon_in_stock',string="No. of Cartoon (Est)",default=1)
    x_product_standard_weight = fields.Float(related='move_id.x_product_standard_weight',string="Packing Spec (kg/pack)",default=10.8,digits = (12,4))