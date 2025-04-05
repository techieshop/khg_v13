# -*- coding: utf-8 -*-
{
    'name': 'RSW Customized Contact for KHG',
    'version': '13.0.0.231110',
    'summary': 'RSW Customized Contact for KHG',
    'sequence': 15,
    'description': "RSW Customized Contact for KHG",
    'category': 'Tools',
    'depends': [ 'stock', ],
    'data': [
        'security/ir.model.access.csv',
        'data/partner_type_data.xml',
        'views/contact_line_number.xml',
        'views/partner_type_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
