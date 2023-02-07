# -*- coding: utf-8 -*-
# from odoo import http


# class PixoraExtensionDdt(http.Controller):
#     @http.route('/pixora_extension_ddt/pixora_extension_ddt', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pixora_extension_ddt/pixora_extension_ddt/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pixora_extension_ddt.listing', {
#             'root': '/pixora_extension_ddt/pixora_extension_ddt',
#             'objects': http.request.env['pixora_extension_ddt.pixora_extension_ddt'].search([]),
#         })

#     @http.route('/pixora_extension_ddt/pixora_extension_ddt/objects/<model("pixora_extension_ddt.pixora_extension_ddt"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pixora_extension_ddt.object', {
#             'object': obj
#         })
