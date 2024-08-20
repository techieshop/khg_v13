# -*- coding: utf-8 -*-

from odoo import fields, models


class CustomCustomPosOrderLine(models.Model):
    _inherit = 'ir.actions.act_window'

    auto_search = fields.Boolean(default=False)


class CustomStockPicking(models.Model):
    _inherit = 'stock.picking'

    picking_type_code = fields.Selection([
        ('incoming', 'Vendors'),
        ('outgoing', 'Customers'),
        ('internal', 'Internal')], related='picking_type_id.code',
        readonly=True, store=True)


