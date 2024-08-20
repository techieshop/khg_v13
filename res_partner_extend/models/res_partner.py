# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResPartnerInherit(models.Model):
    _inherit = "res.partner"

    user_group = fields.Selection([('group_1','Group 1'),('group_2','Group 2'),('group_3','Group 3'),('group_4','Group 4')],string='Group')
    user_group_ids = fields.Many2many('contact.group',string='Group')


class ResUsersInherit(models.Model):
    _inherit = "res.users"

    user_group = fields.Selection([('group_1','Group 1'),('group_2','Group 2'),('group_3','Group 3'),('group_4','Group 4')],string='Group')
    user_group_ids = fields.Many2many('contact.group', string='Group')

    def write(self, vals):
        res = super(ResUsersInherit, self).write(vals)
        self.env['ir.rule'].sudo().clear_cache()
        return res


