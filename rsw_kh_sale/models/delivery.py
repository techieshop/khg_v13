# -*- coding: utf-8 -*-

# from odoo import models, fields, api
from odoo import models, fields

# class rsw_kh_delivery(models.Model):
#     _name = 'rsw_kh_delivery.rsw_kh_delivery'
#     _description = 'rsw_kh_delivery.rsw_kh_delivery'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class kh_delivery(models.Model):
    # _name = 'rsw_kh_delivery.rsw_kh_delivery'
    # _description = 'rsw_kh_delivery.rsw_kh_delivery'
    _inherit = "stock.picking"

    Transporter1 = fields.Many2one("res.partner", string="Transporter 1",)
    Transporter2 = fields.Many2one("res.partner", string="Transporter 2",)
    
    x_cartoon_transfer = fields.Integer(string="Cartoon", default=1)
    x_packing_spec = fields.Float(string="Spec")
    
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100