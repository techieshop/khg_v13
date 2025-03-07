# -*- coding: utf-8 -*-

{
    "name": "Create Product",
    "version": "13.0.1.0.1",
    "description": """
        Sale order form of automatically create best sold product lines
    """,
    "license": "LGPL-3",
    "author": "Milan Hirani",
    "depends": [
        "rsw_tc_sale", "rsw_contact",
    ],
    'data': [
        'views/views.xml',
        'views/js_file.xml',
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
