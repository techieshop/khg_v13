# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Custom Trial Balance Report',
    'version': '13.1.1',
    'summary': 'This module customizes the trial balance report of the accounting module by OdooMates',
    'sequence': 15,
    'description': "This module customizes the trial balance report of the accounting module by OdooMates",
    'category': 'Tools',
    'depends': [
        'om_account_accountant',
        'accounting_pdf_reports'
    ],
    'data': [
        'report/financial_inherit_report.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
