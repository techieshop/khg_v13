# from odoo import api, fields, models, _, tools
# from odoo.exceptions import UserError, ValidationError
# class add_brand(models.Model):
#     _name = 'stock.brand'
#     _description ="stock_brand"
#     name = fields.Char(string='Brand')

#     @api.constrains('name')
#     def check(self):
#         matching_products = self.env['stock.brand'].search([('name', '=', self.name)])
#         if len(matching_products) > 1:
#             raise UserError(_('Brand name already exit'))

# class product_brand(models.Model):
#     _inherit = 'product.template'
#     brand = fields.Many2one('stock.brand',string="Brand")

#     # @api.constrains('name')
#     # def check(self):
#     #     matching_products = self.env['product.template'].search([('name', '=', self.name),('brand','=',self.brand.id),('categ_id','=',self.categ_id.id)])
#     #     if len(matching_products) > 1:
#     #         raise UserError(_('Product with this brand is already exit'))

# class Journal_Entry(models.Model):
#     _inherit = 'account.move'

#     remark =fields.Text(string="Description")