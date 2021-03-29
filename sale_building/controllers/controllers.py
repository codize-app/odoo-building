# -*- coding: utf-8 -*-
# from odoo import http


# class SaleBuilding(http.Controller):
#     @http.route('/sale_building/sale_building/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_building/sale_building/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_building.listing', {
#             'root': '/sale_building/sale_building',
#             'objects': http.request.env['sale_building.sale_building'].search([]),
#         })

#     @http.route('/sale_building/sale_building/objects/<model("sale_building.sale_building"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_building.object', {
#             'object': obj
#         })
