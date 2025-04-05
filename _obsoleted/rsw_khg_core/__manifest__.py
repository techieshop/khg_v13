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
    'version': '13.0.0.20241101',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'contacts', 'sale_stock', 'stock', 'account', 'purchase', 'web'],

    # always loaded
    'data': [
    	"views/assets.xml",
        'views/views.xml',
        'security/res_groups.xml',
        'views/picking.xml',
    ]
}
