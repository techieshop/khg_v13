from datetime import datetime

from odoo import fields, models, api
# #
class CustomPriceListMang(models.Model):
    _inherit = 'product.pricelist'

    temp_name = fields.Char('temp', default='Nop')
class CustomContact(models.Model):
    _inherit = 'res.partner'



    # @api.model
    def change_priceLIst(self):
        print('here we are ready to chang e')
        print('here we are ready to chang e')
        print('here we are ready to chang e')
        print('here we are ready to chang e')
        users = self.env['res.partner'].search([])
        today = datetime.now()
        month = today.month
        year = today.year

        for user in users:
            temp = user.property_product_pricelist
            new_name = 'Default' + '_' + str(year) + '_' + str(month)
            if not user.x_parent_company_code:
                previous = self.env['product.pricelist'].search([('temp_name','=','Default')])
                if previous:
                    previous[0].write({
                        'name': new_name,
                        'display_name': new_name,
                    })
                    user.write({
                        'property_product_pricelist': previous[0].id
                    })
                else:
                    dd=self.env['product.pricelist'].create({
                        'name': new_name,
                        'display_name': new_name,
                        'temp_name':'Default',

                    })
                    user.write({
                        'property_product_pricelist': dd.id
                    })
            else:
                new_name = str(user.x_parent_company_code) + '_' + str(year) + '_' + str(month)
                previous = self.env['product.pricelist'].search([('temp_name', '=', str(user.x_parent_company_code))])
                if (previous):
                    previous[0].write({
                        # 'display_name':  str(user.parent_id),
                        'name' : new_name,
                        'display_name': new_name
                    })
                    user.write({
                        'property_product_pricelist': previous.id
                    })
                else:

                    dd =self.env['product.pricelist'].create({
                        'temp_name': str(user.x_parent_company_code),
                        'name': new_name,
                        'display_name': new_name
                        # 'temp_name': str(user.parent_id.id)
                    })
                    user.write({
                        'property_product_pricelist': dd.id
                    })



