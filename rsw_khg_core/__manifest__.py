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
    'version': '13.0.0.20250401',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'contacts', 'sale_stock', 'stock', 'account','product', 'purchase', 'web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        "views/sale_order.xml",
        "views/purchase_order.xml",
        "views/product.xml",
        "views/product_js.xml",
        "views/stock.xml",
        "views/assets.xml",
        'views/views.xml',
        'security/res_groups.xml',
        'views/picking.xml',
    ]
}
