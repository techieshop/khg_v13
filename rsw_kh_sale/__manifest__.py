# -*- coding: utf-8 -*-
{
    'name': 'RSW Customized Sale Form for KHG',
    'version': '13.0.240220',
    'summary': 'RSW Customized Sale Form for KHG',
    'sequence': 15,
    'description': "RSW Customized Sale Form for KHG",
    'category': 'Tools',
    'depends': ['base','stock','sale','rsw_khg_core'],
    'data': [
        'views/sale_order_view.xml',
        'views/delivery.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
