# -*- coding: utf-8 -*-
{
    'name': "RSW KHG Core",

    'summary': """
        RSW KHG Core""",

    'description': """
        RSW KHG Core
    """,

    'author': "RFID & Security Warehouse",
    'website': "http://www.security-warehouse.com",

    'category': 'Uncategorized',
    'version': '13.0.0.20240410',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'contacts', 'sale_stock', 'account', 'purchase'],

    # always loaded
    'data': [
        'views/views.xml',
        'security/res_groups.xml',
    ]
}
