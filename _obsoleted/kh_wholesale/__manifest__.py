# -*- coding: utf-8 -*-
{
    'name': "KH Wholesale",

    'summary': """
        KH Wholesale""",

    'description': """
        KH Wholesale
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ]
}
