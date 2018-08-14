# -*- coding: utf-8 -*-
from odoo import http

# class PaajafAccount(http.Controller):
#     @http.route('/paajaf_account/paajaf_account/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/paajaf_account/paajaf_account/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('paajaf_account.listing', {
#             'root': '/paajaf_account/paajaf_account',
#             'objects': http.request.env['paajaf_account.paajaf_account'].search([]),
#         })

#     @http.route('/paajaf_account/paajaf_account/objects/<model("paajaf_account.paajaf_account"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('paajaf_account.object', {
#             'object': obj
#         })