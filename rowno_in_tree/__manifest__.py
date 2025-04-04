# -*- encoding: utf-8 -*-
{
    'name': "Row Number in tree/list view",
    'version': '13.0.0.4',
    'summary': 'Show row number in tree/list view.',
    'category': 'Other',
    'description': """By installing this module, user can see row number in Odoo backend tree view. sequence in list, Numbering List View, row count, row counting, show count list, list view row count, number in row, rij nummer, номер строки, numéro de ligne, Zeilennummer, numero de fila, رقم الصف , nomor baris, ListView Row Count,list view row number, number in list view, tree row number, tree view row number, list view row number, dynamic sequence, dynamic row number, line sequence, sequence in report, record count, dynamic list view, dynamic tree view, dynamic listview, listview advance, list editor, list row sequence, backup, sticky, document, list view number, listview number, list number, tree number, treeview number, stick list, row number report, sequence number, sequencial number, number in list""",

    "depends" : ['web'],
    'data': [
             'views/listview_templates.xml',
             ],
    "images": ["static/description/rowno_tree-banner.png"],

    # Author
    'author': 'Synodica Solutions Pvt. Ltd.',
    'website': 'https://synodica.com',
    'maintainer': 'Synodica Solutions Pvt. Ltd.',

    'license': 'LGPL-3',
    'qweb': [
            ],  
    
    'installable': True,
    'application'   : True,
    'auto_install'  : False,
}
