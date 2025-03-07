from odoo import api, fields, models


class KHGSaleOrder(models.Model):
    _inherit = 'sale.order'

    def compute_partners(self):
        type_id = self.env.ref('rsw_contact.partner_type_customer', raise_if_not_found=False)
        return self.env['res.partner'].search([]).filtered(lambda m: type_id.id in m.newtype.ids).ids

    partners = fields.Many2many(
        comodel_name='res.partner',
        default=compute_partners,
        string='Partners')
