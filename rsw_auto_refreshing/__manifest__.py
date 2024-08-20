# -*- coding: utf-8 -*-

{
    'name': 'RSW For Self Refreshing',
    'version': '0.1',
    'depends': [
        'web',
        'bus',
        'mail',
        'base_automation',
        'stock',
    ],
    'author': 'Landry Dieudonne',
    'website': '',
    'license': 'AGPL-3',
    'description': """""",
    'category': 'Tools',
    'data': [
        'datas/data.xml',
        'views/webclient_templates.xml',
        'views/view_action.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'sequence': 10,
    'auto_install': False,
}
