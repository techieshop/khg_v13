# -*- coding: utf-8 -*-
{
    'name': "Account PDF Reports",

    'summary': """
        Account PDF Reports(Multi-Company support)""",

    'description': """
        Account PDF Reports(Multi-Company support)
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'accounting_pdf_reports'],

    # always loaded
    'data': [
        'views/views.xml',
    ]
}
