# -*- coding: utf-8 -*-
{
    'name': "RSW KHG Product Custom",

    'summary': """
        Enhancement to product customized for KHG    
    """,

    'description': """
        Enhancement to product customized for KHG    
    """,

    'author': "RFID & Security Warehouse",
    'website': "http://www.security-warehouse.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '13.0.0.231107',

    # any module necessary for this one to work correctly
    'depends': ['base','product',"purchase","stock","sale",'sale_stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        "views/sale_order.xml",
        "views/purchase_order.xml",
        "views/product.xml",
        "views/stock.xml",
        "views/assets.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
