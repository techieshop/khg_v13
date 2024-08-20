# -*- coding: utf-8 -*-
{
    'name': "rsw_kh_delivery",

    'summary': """
        Customize the delivery process for KH
    """,

    'author': "RSW",
    'website': "http://www.security-warehouse.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '13.0.0.231110',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/delivery.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
