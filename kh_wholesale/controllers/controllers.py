# -*- coding: utf-8 -*-
# from odoo import http


# class KhWholesale(http.Controller):
#     @http.route('/kh_wholesale/kh_wholesale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kh_wholesale/kh_wholesale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kh_wholesale.listing', {
#             'root': '/kh_wholesale/kh_wholesale',
#             'objects': http.request.env['kh_wholesale.kh_wholesale'].search([]),
#         })

#     @http.route('/kh_wholesale/kh_wholesale/objects/<model("kh_wholesale.kh_wholesale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kh_wholesale.object', {
#             'object': obj
#         })
