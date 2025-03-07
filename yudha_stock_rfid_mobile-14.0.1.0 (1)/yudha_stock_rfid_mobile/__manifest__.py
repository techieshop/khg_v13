# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Yudha Stock RFID in Mobile',
    'category': 'Inventory/Inventory',
    'summary': 'Yudha Stock RFID scan in Mobile',
    'version': '1.0',
    'description': """ """,
    'depends': [ 'web_mobile'],
    'qweb': ['static/src/xml/yudha_stock_mobile_rfid.xml'],
    'data': ['views/yudha_stock_rfid_template.xml'],
    'installable': True,
    'auto_install': True,
    'license': 'OPL-1',
}
