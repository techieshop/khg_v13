from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = "sale.order.line"

    # delivery_department_id = fields.Many2one("delivery.department")
    tc_stock_picking_ids = fields.Many2many("stock.picking")

    # @api.depends('qty_delivered_method', 'qty_delivered_manual', 'analytic_line_ids.so_line',
    #              'analytic_line_ids.unit_amount', 'analytic_line_ids.product_uom_id')
    # def _compute_qty_delivered(self):
    #     print(self)
