# -*- coding: utf-8 -*-
# from odoo import http


# class RswPossearchSerial(http.Controller):
#     @http.route('/rsw_possearch_serial/rsw_possearch_serial/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rsw_possearch_serial/rsw_possearch_serial/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rsw_possearch_serial.listing', {
#             'root': '/rsw_possearch_serial/rsw_possearch_serial',
#             'objects': http.request.env['rsw_possearch_serial.rsw_possearch_serial'].search([]),
#         })

#     @http.route('/rsw_possearch_serial/rsw_possearch_serial/objects/<model("rsw_possearch_serial.rsw_possearch_serial"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rsw_possearch_serial.object', {
#             'object': obj
#         })
