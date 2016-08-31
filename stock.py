from openerp import models, fields, api

class stock_picking(models.Model):
	_inherit = "stock.picking"

	partner_do = fields.Char("Nomor DO Supplier:")