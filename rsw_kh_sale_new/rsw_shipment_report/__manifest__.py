# -*- coding: utf-8 -*-
{
    'name': "RSW Shipment Report",
    'summary': """
        RSW Shipment Report""",
    'description': """
        RSW Shipment Report
    """,
    'author': "Dennis Chan",
    'category': 'Uncategorized',
    'version': '13.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['rsw_shipment_management','purchase','rsw_internal_transaction'],

    # always loaded
    'data': [
        'views/shipment_report.xml',
        'views/purchase_report.xml'
    ],
    "installable": True,
    'application': True,
}
