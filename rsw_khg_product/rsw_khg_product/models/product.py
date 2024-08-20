# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class rsw_khg_product(models.Model):
#     _name = 'rsw_khg_product.rsw_khg_product'
#     _description = 'rsw_khg_product.rsw_khg_product'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class product_khg(models.Model):
    
    _inherit = 'product.template'

    x_product_khg_grade = fields.Selection(selection=[
        ('NO_GRADE', '--'),
        ('GRADE_1', '一級'),
        ('GRADE_2', '二級'),
        ('GRADE_3', '三級'),
        ], string='Product Grade',default='NO_GRADE')
    
    x_country_of_origin = fields.Selection(selection=[
        ('au','澳洲'),
        ('br','巴西'),
        ('cn','中國'),
        ('my', '馬來西亞'),
        ('nz','新西蘭'),
        ('vn', '越南'),
        ], string='Country of Origin')
    
    x_product_standard_weight = fields.Float(string="Packing Spec (kg/pack)",default=10.8,digits = (12,4))
    
    x_estimated_cartoon_in_stock = fields.Integer(compute='_compute_x_estimated_cartoon_in_stock', string='Cartoon')
    
    @api.depends('x_product_standard_weight')
    def _compute_x_estimated_cartoon_in_stock(self):
        for record in self:
            record.x_estimated_cartoon_in_stock=int(round(record.qty_available/record.x_product_standard_weight))