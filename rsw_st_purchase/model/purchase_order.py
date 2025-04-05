from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def compute_partners(self):
        type_id = self.env.ref('rsw_khg_core.partner_type_supplier', raise_if_not_found=False)
        return self.env['res.partner'].search([]).filtered(lambda m: type_id.id in m.newtype.ids).ids

    partners = fields.Many2many(
        comodel_name='res.partner',
        default=compute_partners,
        string='Partners')


    lc_no = fields.Char('L/C No.')
    bl_no = fields.Char(String="B/L #")
    is_shipment = fields.Boolean(
        string='Shipment', default=True, store=True, copy=False)
    container_no = fields.Char(string='Container #', copy=False, )
    # container_no = fields.Many2one('purchase.order.shipment',string='Container No.', related='purchase.order.shipment.container_no' )
    scheduled_arrival = fields.Datetime(string='')
    shipment_date = fields.Datetime(string='')
