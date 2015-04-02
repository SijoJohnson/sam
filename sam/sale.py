from openerp.osv import fields, osv
from openerp import tools


class sale_order(osv.osv):
    _inherit = 'sale.order'
    
    
    def _get_users_shop(self, cr, uid, context=None):
        user_obj = self.pool.get('res.users')
        return user_obj.browse(cr, uid, uid).shop_id.id
         
    
    _columns = {
                    'shop_id'           :   fields.many2one('sale.shop', 'Shop', readonly= True, required=True),
                    'discount_amount'   :   fields.float('Discount Amount'),
                }
    _defaults = {
                    'shop_id'           :   _get_users_shop,
                 }
    
    def create(self, cr, uid, vals, context=None):
        shop_obj = self.pool.get('sale.shop')
        shop_code = shop_obj.browse(cr, uid, vals['shop_id']).code
        
        new_id = super(sale_order, self).create(cr, uid, vals, context=None)
        order_name = vals['name'].replace('SO', 'SO-'+str(shop_code)+'-')
        self.write(cr, uid, new_id, {'name' : order_name})
        return new_id
    
sale_order()
    
    

    
    
class sale_shop(osv.osv):
    _name = 'sale.shop'
    _columns = {
                    'name'              :   fields.char("Branch Name", size=64, required=True),
                    'code'              :   fields.char("Branch Name", size=64, required=True),
                    'warehouse_id'      :   fields.many2one('stock.warehouse', 'Warehouse', required=True),
                    
                }
    
    _sql_constraints = [
                ('name_code_uniq', 'unique(code)', 'The code must be unique per shop!'),
        ]

    
sale_shop()    