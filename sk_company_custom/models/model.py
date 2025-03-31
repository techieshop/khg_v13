from odoo import models
from odoo.http import request

class Http(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        res = super().session_info()
        user = request.env.user
        res['display_switch_company_menu'] = user.has_group('base.group_multi_company') and len(user.company_ids) > 0
        return res
