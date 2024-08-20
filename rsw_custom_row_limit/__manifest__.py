# -*- coding: utf-8 -*-
{
    'name': "RSW List View Row Limit",

    'summary': """
        RSW List View Row Limit    
    """,

    'description': """
        List View Row Limit    
    """,

    'author': "RSW",
    'website': "https://www.security-warehouse.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '13.0.0.240102',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        "views/assets.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
