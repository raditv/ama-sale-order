from openerp.osv import osv, fields

class sale_order(osv.Model):
	_name 	= 'sale.order'
	_inherit= 'sale.order'
	_columns= {
		'order_sheet_no' : fields.char("No. OS/DN", size=100),
		'customer_po_no' : fields.char("No. PO", size=100)
	}