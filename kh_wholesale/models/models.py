from odoo import models, fields, api


class KHWholesale(models.Model):
    _name = 'kh.wholesale'
    _description = 'KH Wholesale'

    name = fields.Char()