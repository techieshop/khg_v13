# -*- coding: utf-8 -*-
{
    'name': "RSW TC Sale",

    'summary': """
        RSW TC Sale""",

    'description': """
        RSW TC Sale
    """,

    'author': "RFID & Security Warehouse",
    'website': "http://www.security-warehouse.com",

    'category': 'Uncategorized',
    'version': '13.0.0.20240410',

    # any module necessary for this one to work correctly
    'depends': ['rsw_khg_core','base', 'sale', 'contacts', 'sale_stock', 'sale_management', 'purchase', 'mrp','accounting_pdf_reports'],
    
    'web.assets_backend': [        
        'static/src/css/kanban.css',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/stock_picking_view.xml',
    ]
}
