# -*- coding: utf-8 -*-
{
    'name': "RSW Shipment Report",
    'summary': """
        RSW Shipment Report""",
    'description': """
        RSW Shipment Report
    """,
    'author': "Milan Hirani",
    'category': 'Uncategorized',
    'version': '13.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['rsw_shipment_management'],

    # always loaded
    'data': [
        'views/shipment_report.xml'
    ],
    "installable": True,
    'application': True,
}
