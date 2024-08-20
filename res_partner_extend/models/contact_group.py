from odoo import fields, models, api


class ContactGroup(models.Model):
    _name = 'contact.group'
    _description = 'Description'

    name = fields.Char('Group Name')
