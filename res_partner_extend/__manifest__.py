{
    'name': 'Contact Extend',
    'category': 'Contact',
    'summary': 'Custom Recoed Rule',
    'version': '13.0.1',
    'author': 'Bansi',
    'depends': ['base','contacts'],
    'data': [
        'security/ir.model.access.csv',
        'security/partner_security.xml',
        'views/contact_group_view.xml',
        'views/res_partner_view.xml',
    ],
    'installable': True,
    'application': False
}
