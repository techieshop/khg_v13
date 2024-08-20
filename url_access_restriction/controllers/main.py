# -*- coding: utf-8 -*-
import logging
from odoo import http
from odoo.http import request
from odoo.addons.web.controllers import main
from odoo.exceptions import Warning
import logging

_logger = logging.getLogger(__name__)

class UrlAction(main.Action):

	@http.route()
	def load(self, action_id, additional_context=None):
		menu = False
		menu_ids = request.env['ir.ui.menu'].sudo().search([])
		for menu_id in menu_ids:
			if menu_id.action:
				if menu_id.action.id == action_id:
					menu = menu_id
		user = request.env['res.users'].sudo().browse(request.session.uid)
		if not self._user_has_acces_right(action_id, menu, user):
			raise Warning('Access Denied, Please Contact The System Administrator')

		return super(UrlAction, self).load(action_id, additional_context=additional_context)


	def _user_has_acces_right(self, action_id, menu, user):
		action = request.env['ir.actions.act_window'].sudo().search([('id','=',action_id)], limit=1)
		if action and len(action.groups_id) > 0:
			if any(elem in user.groups_id.ids  for elem in action.groups_id.ids):
				return True
			return False
		if menu and len(menu.groups_id.ids) > 0:
			if any(elem in user.groups_id.ids  for elem in menu.groups_id.ids):
				return True
			return False
		if menu and menu.parent_id:
			return self._user_has_acces_right(action_id, menu.parent_id, user)

		return True
