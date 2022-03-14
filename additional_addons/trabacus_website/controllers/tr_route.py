# # -*- coding: utf-8 -*-
# # Part of Odoo. See LICENSE file for full copyright and licensing details.
# from odoo import http
# from odoo.http import request
# from odoo.addons.Rebolt_Network.controllers import rn_main_API
# from odoo.addons.Rebolt_Network.models.rn_config_global import rebolt_config_global as rg
#
# def get_page_settings(self, url):
#     page_settings = {}
#     pgs_obj = self.env['rebolt.page.settings'].sudo()
#     ps = pgs_obj.search([('url', '=', url)])
#     if ps:
#         pgs = ps[0]
#         page_settings.update({
#             'title': pgs.title,
#             'url': pgs.url,
#             'image_url': pgs.image_url,
#             'description': pgs.description,
#             'keywords': pgs.keywords
#         })
#
#     return page_settings
#
# class RN_ROUTE_INDEX(rn_main_API.RN_Main_API):
#
#     @http.route('/', type='http', auth="public", website=True, sitemap=True)
#     def index(self, *args, **kw):
#         page_url = request.httprequest.path
#         pgs = get_page_settings(request, page_url)
#         return request.render('Rebolt_Website.rn_index', {'pgs' : pgs})
#
# class RN_ROUTE(http.Controller):
#
#     @http.route('/index', type='http', auth="public", website=True, sitemap=True)
#     def index(self, *args, **kw):
#         page_url = request.httprequest.path
#         pgs = get_page_settings(request, page_url)
#         return request.render('Rebolt_Website.rn_index', {'pgs' : pgs})
#
#     @http.route('/download', type='http', auth="public", website=True, sitemap=True)
#     def download(self, *args, **kw):
#         page_url = request.httprequest.path
#         pgs = get_page_settings(request, page_url)
#         return request.render('Rebolt_Website.rn_download', {'pgs' : pgs})
#
#     @http.route('/pricing', type='http', auth="public", website=True, sitemap=True)
#     def pricing(self, *args, **kw):
#
#         cr = request.cr
#         state_obj = request.env['res.country.state']
#
#         states = state_obj.sudo().search_read([('country_id', '=', request.env.company.country_id.id), ('charging_fee', '>', 0)],
#                                               ['code','name','charging_fee'])
#         loc_sql = "SELECT min(parking_fee) as parking_fee, min(idling_fee) as idling_fee FROM rebolt_locations"
#         cr.execute(loc_sql)
#         loc_data = cr.dictfetchone()
#         parking_fee = loc_data.get('parking_fee')
#         idling_fee = loc_data.get('idling_fee')
#
#         page_url = request.httprequest.path
#         pgs = get_page_settings(request, page_url)
#
#         data = {
#             'states' : states,
#             'parking_fee' : parking_fee,
#             'idling_fee' : idling_fee,
#             'pgs': pgs
#         }
#         return request.render('Rebolt_Website.rn_pricing', data)
#
#     @http.route('/faqs', type='http', auth="public", website=True, sitemap=True)
#     def faqs(self, *args, **kw):
#         page_url = request.httprequest.path
#         pgs = get_page_settings(request, page_url)
#         return request.render('Rebolt_Website.rn_faqs', {'pgs' : pgs})
#
#     @http.route('/host', type='http', auth="public", website=True, sitemap=True)
#     def host(self, *args, **kw):
#         page_url = request.httprequest.path
#         pgs = get_page_settings(request, page_url)
#         return request.render('Rebolt_Website.rn_host', {'pgs' : pgs})
#
#     @http.route('/aboutus', type='http', auth="public", website=True, sitemap=True)
#     def aboutus(self, *args, **kw):
#         page_url = request.httprequest.path
#         pgs = get_page_settings(request, page_url)
#         return request.render('Rebolt_Website.rn_aboutus', {'pgs': pgs})
#
#     @http.route('/privacy', type='http', auth="public", website=True, sitemap=True)
#     def privacy(self, *args, **kw):
#         page_url = request.httprequest.path
#         pgs = get_page_settings(request, page_url)
#         return request.render('Rebolt_Website.rn_privacy', {'pgs' : pgs})
#
#     @http.route('/terms', type='http', auth="public", website=True, sitemap=True)
#     def terms(self, *args, **kw):
#         page_url = request.httprequest.path
#         pgs = get_page_settings(request, page_url)
#         return request.render('Rebolt_Website.rn_terms', {'pgs' : pgs})
#
#     @http.route('/sendmessage', type='json', auth="public", csrf=False)  # WEB
#     def sendmessage(self, **post):
#         reqData = request.jsonrequest
#         comp = request.env.company
#         env = request.env
#
#         lead_obj = env['crm.lead']
#         lead_vals = {
#             'name' : reqData.get('name'),
#             'email_from': reqData.get('email'),
#             'phone': reqData.get('phone'),
#             'description': reqData.get('message')
#         }
#         lead = lead_obj.sudo().create(lead_vals)
#         rg.send_mail_tempalte(request, 'Rebolt_Website.mail_template_contactus', lead.id, force_send=True)
#         result_data = {
#             'success' : True
#         }
#         return result_data
