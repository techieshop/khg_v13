{
    'name': 'Product Barcode',
    'version': '13.0.0.1',
    'license': 'LGPL-3',
    'category': 'Generate Sold Product Report',
    'summary': "Manage Employee Payroll",
    'depends': ['sale_management', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_sold_report.xml',
        'wizard/tc_sale_report_wizard_view.xml',
    ],
    'installable': True,
}
