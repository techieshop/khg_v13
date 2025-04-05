# -*- coding: utf-8 -*-
{
    'name': "RSW Delivery Report",
    'summary': """
        RSW Delivery Report""",
    'description': """
        RSW Delivery Report
    """,
    'author': "RFID Security-Warehouse",
    'category': 'Uncategorized',
    'version': '13.0.0.20240821',

    # any module necessary for this one to work correctly
    'depends': ['rsw_tc_sale'],

    # always loaded
    'data': [
        'views/res_partner.xml'
    ],
    "installable": True,
    'application': True,
}
