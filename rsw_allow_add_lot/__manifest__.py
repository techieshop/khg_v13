# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'RSW - Allow add/modify lot',
    'version': '13.0.5.0.0',
    'category': 'Stock',
    'summary': 'Allow add/modify lot after stock picking confirmation',

    'license': 'LGPL-3',
    'website': 'www.security-warehouse.com',
    'depends': ['stock'],
    'demo': [],
    'data': [
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'qweb': [],
}
