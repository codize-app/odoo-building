# -*- coding: utf-8 -*-
# from odoo import http


# class PartnerTools(http.Controller):
#     @http.route('/partner_tools/partner_tools/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_tools/partner_tools/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_tools.listing', {
#             'root': '/partner_tools/partner_tools',
#             'objects': http.request.env['partner_tools.partner_tools'].search([]),
#         })

#     @http.route('/partner_tools/partner_tools/objects/<model("partner_tools.partner_tools"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_tools.object', {
#             'object': obj
#         })
