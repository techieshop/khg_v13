from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    # delivery_department_id = fields.Many2one("delivery.department")
    restaurant_department = fields.Selection([('kitchen','廚'),('dimsum','點'),('bbq','味'),('thai','泰'),('hotpot','火'),('porridge','粥'),('fook','福'),('bake','燒'),('bar','吧'),('dai','代')],'Restaurant Department',Default='kitchen')
    tc_sale_order_line = fields.Char()

    def action_done(self):
        if self._context.get('partner_transfer') == True:
            order_lines = self.partner_id.sale_order_line_ids
            for line in self.move_ids_without_package.filtered(lambda x: x.quantity_done):
                order_line = order_lines.filtered(lambda x: x.product_id.id == line.product_id.id).sorted('qty_to_deliver')
                for ol in order_line.filtered(lambda x: x.qty_to_deliver >= line.quantity_done):
                    old_picking = ol.order_id.picking_ids.filtered(lambda x: x.state != 'done').sudo()
                    if old_picking:
                        old_picking.action_cancel()
                        old_picking.unlink()
                    # if not line.picking_id.sale_id:
                    #     ol.order_id.picking_ids = [(4, self.id)]
                    line.sale_line_id = ol.id
                    break
        return super(StockPicking, self).action_done()
