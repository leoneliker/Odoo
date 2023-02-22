# -*- coding: utf-8 -*-
# from odoo import http


# class AlmendritaIker(http.Controller):
#     @http.route('/almendrita__iker/almendrita__iker', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/almendrita__iker/almendrita__iker/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('almendrita__iker.listing', {
#             'root': '/almendrita__iker/almendrita__iker',
#             'objects': http.request.env['almendrita__iker.almendrita__iker'].search([]),
#         })

#     @http.route('/almendrita__iker/almendrita__iker/objects/<model("almendrita__iker.almendrita__iker"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('almendrita__iker.object', {
#             'object': obj
#         })
