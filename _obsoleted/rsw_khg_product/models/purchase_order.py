from odoo import fields, models, api


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    x_po_cartoon = fields.Integer(string="Cartoon",default=1)
    x_product_standard_weight = fields.Float(string="Packing Spec (kg/pack)",default=10.8)

    # x_cartoon field data purchase to Transfer
    def _create_stock_moves(self, picking):
        res = super(PurchaseOrderLine, self)._create_stock_moves(picking)
        for move in res:
            linked_po=self.filtered(lambda m:m.id == move.purchase_line_id.id)
            if linked_po:
                move.x_po_cartoon = linked_po[0].x_po_cartoon
        return res

    @api.onchange('x_product_standard_weight', 'x_po_cartoon')
    def onchange_cartoon(self):
        if self.x_product_standard_weight and self.x_po_cartoon:
            self.product_qty = self.x_product_standard_weight * self.x_po_cartoon
