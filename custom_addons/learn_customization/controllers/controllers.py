# -*- coding: utf-8 -*-
# from odoo import http


# class LearnCutomization(http.Controller):
#     @http.route('/learn_cutomization/learn_cutomization', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/learn_cutomization/learn_cutomization/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('learn_cutomization.listing', {
#             'root': '/learn_cutomization/learn_cutomization',
#             'objects': http.request.env['learn_cutomization.learn_cutomization'].search([]),
#         })

#     @http.route('/learn_cutomization/learn_cutomization/objects/<model("learn_cutomization.learn_cutomization"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('learn_cutomization.object', {
#             'object': obj
#         })

