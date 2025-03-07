# -*- coding: utf-8 -*-
# from odoo import http


# class RswKhDelivery(http.Controller):
#     @http.route('/rsw_kh_delivery/rsw_kh_delivery/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rsw_kh_delivery/rsw_kh_delivery/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rsw_kh_delivery.listing', {
#             'root': '/rsw_kh_delivery/rsw_kh_delivery',
#             'objects': http.request.env['rsw_kh_delivery.rsw_kh_delivery'].search([]),
#         })

#     @http.route('/rsw_kh_delivery/rsw_kh_delivery/objects/<model("rsw_kh_delivery.rsw_kh_delivery"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rsw_kh_delivery.object', {
#             'object': obj
#         })
