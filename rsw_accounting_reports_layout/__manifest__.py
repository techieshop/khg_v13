# -*- coding: utf-8 -*-
{
    'name': "RSW Account PDF Reports Customization for Multi-Company Setup",

    'summary': """
        RSW Account PDF Reports Customization for Multi-Company Setup""",

    'description': """
        RSW Account PDF Reports Customization for Multi-Company Setup
    """,

    'author': "My Company",
    'website': "http://www.security-warehouse.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'accounting_pdf_reports'],

    # always loaded
    'data': [
        'views/views.xml',
    ]
}
