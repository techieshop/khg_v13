# -*- coding: utf-8 -*-
# from odoo import http


# class RswKhgProduct(http.Controller):
#     @http.route('/rsw_khg_product/rsw_khg_product/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rsw_khg_product/rsw_khg_product/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rsw_khg_product.listing', {
#             'root': '/rsw_khg_product/rsw_khg_product',
#             'objects': http.request.env['rsw_khg_product.rsw_khg_product'].search([]),
#         })

#     @http.route('/rsw_khg_product/rsw_khg_product/objects/<model("rsw_khg_product.rsw_khg_product"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rsw_khg_product.object', {
#             'object': obj
#         })
