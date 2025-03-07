# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "RSW Custom PL and BS Report Wizard",
    "version": "13.1.1.231222",
    "summary": "",
    "sequence": 15,
    "description": "",
    "category": "Tools",
    "depends": [
        "om_account_accountant",
        "accounting_pdf_reports"
    ],
    "data": [
        "report/financial_inherit_report.xml",
        "views/account_financial_report.xml",
        "views/account_account_type.xml",
        "wizards/accounting_report.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
