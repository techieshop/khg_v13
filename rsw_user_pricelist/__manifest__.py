# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Change User Price LIst',
    'version': '13.1.1',
    'summary': 'customized Contact Price List',
    'sequence': 15,
    'description': "",
    'category': 'Tools',
    'depends': [ 'product'
    ],
    'data': [
        'views/contact.xml',
        'security/security.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
