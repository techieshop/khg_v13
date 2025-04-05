
from odoo import fields, models, api
class CustomContact(models.Model):
    _inherit = 'res.partner'
    _rec_name = 'reference_number'
    _order = 'reference_number asc'

    company = fields.Many2many('res.company')
    newtype = fields.Many2many(
        comodel_name='partner.type',
        string='Type')
    fax = fields.Char(string="Fax")
    nickname = fields.Char(string="Nickname")
    delivery_line_number = fields.Integer(string="Delivery Line Number")
    reference_number = fields.Integer(string="Reference Number", default=0)
    reference_name = fields.Char(string="Reference Name", compute="_compute_reference_name", store=False, required=True)

    @api.depends("name","reference_number")
    def _compute_reference_name(self):
        for record in self:
            if record.name:
                record.reference_name = record.name + " " + "[" + str(record.reference_number) + "]"

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, '%s' % (record.reference_name)))
        return result

