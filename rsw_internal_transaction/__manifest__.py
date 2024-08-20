# -*- coding: utf-8 -*-

{
    'name' : "RSW Create Internal Transaction",
    'version' : "13.0",
    'category' : "Purchases",
    'summary': 'This apps helps to Covert Purchase order from Sales Order and sale order from purchase order',
    'description' : """
            RSW Create Internal Transactions
     """,
    'author' : "RFID & Security Warehouse",
    'website'  : "https://www.security-warehouse.com",
    'depends'  : [ 'base','sale_management','purchase','mail'],
    'data'     : [  'security/ir.model.access.csv',
                    'security/res_groups.xml',
                    'wizard/purchase_order_wizard_view.xml',
                    'wizard/sale_order_wizard_view.xml',
                    'views/inherit_sale_order_view.xml',
                    'views/main_purchase_order_view.xml',
            ],      
    'installable' : True,
    'application' :  False,
}
