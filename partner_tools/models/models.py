# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
	_inherit = 'res.partner'

	product_ids = fields.One2many("product.tool.line", "partner_id", "Herramientas", help="Herramientas que tiene el Contacto.")

class ProductToolLine(models.Model):
	_name = 'product.tool.line'

	product_id = fields.Many2one('product.product', 'Herramienta')
	qty = fields.Float('Cantidad')
	partner_id = fields.Many2one('res.partner', 'Contacto')
