# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class rsw_possearch_serial(models.Model):
#     _name = 'rsw_possearch_serial.rsw_possearch_serial'
#     _description = 'rsw_possearch_serial.rsw_possearch_serial'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
