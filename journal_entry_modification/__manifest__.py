# -*- coding: utf-8 -*-
{
    'name': "Journal Entry Modification",
    'summary': """
        Modifications in the journal entry view to accommodate additional fields""",

    'author': "Marc De Costa",
    'license': 'AGPL-3',
    'category': 'Accounting',
    'version': '1.0',
    'depends': ['base','om_account_accountant'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_move.xml',
    ],
    'installable': True,
}
