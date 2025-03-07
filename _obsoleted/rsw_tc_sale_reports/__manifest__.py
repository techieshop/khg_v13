{
    'name': 'Sold Product Report',
    'version': '13.0.0.1',
    'license': 'LGPL-3',
    'category': 'Sales/Sales',
    'summary': "Generate Sold Product Report",
    'description': """
This module prints all the product that is delivered by date.
    """,
    # 'depends': ['sale_management', 'stock', 'rsw_tc_sale'],
    'depends': ['sale_management', 'stock'],

    'data': [
        'security/ir.model.access.csv',
        'views/sale_sold_report.xml',
        'wizard/sold_product_report_wizard_view.xml',
    ],
    'installable': True
}
