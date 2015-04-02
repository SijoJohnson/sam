from openerp.osv import fields, osv
from openerp import tools

class res_users(osv.osv):
    _inherit = 'res.users'
    _columns = {
                    'shop_id'           :   fields.many2one('sale.shop', 'Shop', required=True),
                }
res_users()