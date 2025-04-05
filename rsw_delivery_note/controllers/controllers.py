# -*- coding: utf-8 -*-
# from odoo import http


# class RswDeliveryNote(http.Controller):
#     @http.route('/rsw_delivery_note/rsw_delivery_note/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rsw_delivery_note/rsw_delivery_note/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rsw_delivery_note.listing', {
#             'root': '/rsw_delivery_note/rsw_delivery_note',
#             'objects': http.request.env['rsw_delivery_note.rsw_delivery_note'].search([]),
#         })

#     @http.route('/rsw_delivery_note/rsw_delivery_note/objects/<model("rsw_delivery_note.rsw_delivery_note"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rsw_delivery_note.object', {
#             'object': obj
#         })
