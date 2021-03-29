# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
	_inherit = 'sale.order'

	build_ids = fields.One2many("sale.build.line", "sale_id", "Certificaciones", help="Certificaciones para el cumplimiento del Proyecto.")

class SaleBuildLine(models.Model):
	_name = 'sale.build.line'

	def _compute_amount(self):
		for rec in self:
			total = 0
			for build in rec.sale_id.build_ids:
				total += build.percentage
			if total > 100:
				raise ValidationError('El porcentaje total es mayor a 100 %')
			rec.amount = (rec.percentage * rec.sale_id.amount_total) / 100

	sale_id = fields.Many2one('sale.order', 'Sale ID')
	stage = fields.Char('Etapa')
	percentage = fields.Float('Porcentaje')
	amount = fields.Float('Monto', readonly="True", compute="_compute_amount")
