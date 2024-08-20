# -*- coding: utf-8 -*-
{
    'name': 'RSW Purchase Order Shipment',
    'summary': "Create Shipments of Purchase Order, print shipment report and align stock transfer as per shipments",
    'author': "Dennis Chan",
    'website': "https://www.security-warehouse.com",

    'license': 'OPL-1',
    'category': 'Purchase',
    'version': '13.0.0.1',

    'depends': ['base', 'purchase', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'security/purchase_order_shipment_security.xml',

        'data/data.xml',

        'views/purchase_order.xml',
        'views/purchase_order_shipment.xml',
        'views/stock_picking.xml',
        'report/shipment_handling_report.xml',
        'report/report.xml',
    ],
    'images': ['/static/description/sw-key-logo-512.jpg'],

    'application': True,
    'installable': True,
    'currency': 'USD'
}
