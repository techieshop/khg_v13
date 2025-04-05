# -*- coding: utf-8 -*-

{
    'name': 'RSW Delivery Note',
    'version': '0.1',
    'depends': [
        'stock',
        'sale',
    ],
    'author': 'Landry Dieudonne',
    'website': '',
    'license': 'AGPL-3',
    'description': """""",
    'category': 'Tools',
    'data': [
        'views/template_report.xml',
        'views/delivery.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'sequence': 10,
    'auto_install': False,
}
