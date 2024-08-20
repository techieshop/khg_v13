# -*- coding: utf-8 -*-
{
    'name': "RSW POS Auto Purchase",
    'summary': """RSW POS Auto Purchase""",
    'description': """
        Custome Module for POS Auto Purchase
    """,
    'author': "Landry Dieudonne",
    'website': "https://www.clodoo.com",
    'category': 'tools',
    'version': '0.1',
    'depends': ['point_of_sale', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],

    'installable': True,
    'application': True,
    'sequence': 10,
    'auto_install': False,
    'license': 'LGPL-3',
}
