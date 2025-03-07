# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Print Journal Entries Report in Odoo',
    'version': '13.0.0.0',
    'category': 'Account',
    'summary': 'Allow to print pdf report of Journal Entries.',
    'description': """
    Allow to print pdf report of Journal Entries.
    journal entry
    print journal entry 
    journal entries
    print journal entry reports
    account journal entry reports
    journal reports
    account entry reports

    
""",
    'price': 000,
    'currency': 'HKD',
    'author': 'RFID and Security Warehouse',
    'website': 'https://www.security-warehouse.com',
    'depends': ['base','account','accounting_pdf_reports'],
    'data': [
            'report/report_journal_entries.xml',
            'report/report_journal_entries_view.xml',
             'wizard/journal_entry_report_wizard.xml',
    ],
    'installable': True,
    'auto_install': False,
    'live_test_url':'',
    "images":["static/description/Banner.png"],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
