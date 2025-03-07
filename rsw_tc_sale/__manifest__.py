# -*- coding: utf-8 -*-
{
    'name': "RSW TC Sale",
    'version': '13.0.0.1.20241026',
    'license': 'LGPL-3',
    'category': 'Sales/Sales',
    'summary': """
        RSW TC Sale""",
    'description': """
        RSW TC Sale
    """,
    'author': "RFID & Security Warehouse",
    'website': "http://www.security-warehouse.com",
    # any module necessary for this one to work correctly
    'depends': ['rsw_khg_core','base', 'sale', 'stock', 'contacts', 'sale_stock', 'sale_management', 'purchase', 'mrp','accounting_pdf_reports', 'rsw_contact'],  
    'web.assets_backend': [        
        'static/src/css/kanban.css',
    ],
    'css': [      
        'static/src/css/kanban.css',
    ],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sale_js.xml',
        'views/main_view.xml',
        'views/res_partner_sale_instant.xml',
        'views/stock_picking_view.xml',
        'report/delivery.xml',
        'views/delivery_report.xml',
        'report/sale_sold_report.xml',
        'report/template_report.xml',
        'wizard/sold_product_report_wizard_view.xml',        
    ],
    'installable': True,
}
