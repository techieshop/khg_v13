# -*- coding: utf-8 -*-
# from odoo import http


# class TcSales(http.Controller):
#     @http.route('/tc_sales/tc_sales/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tc_sales/tc_sales/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tc_sales.listing', {
#             'root': '/tc_sales/tc_sales',
#             'objects': http.request.env['tc_sales.tc_sales'].search([]),
#         })

#     @http.route('/tc_sales/tc_sales/objects/<model("tc_sales.tc_sales"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tc_sales.object', {
#             'object': obj
#         })
