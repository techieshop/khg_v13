from odoo import api, fields, models


class PartnerType(models.Model):
    _name = 'partner.type'
    _description = 'Partner Type'

    name = fields.Char()

