{
    "name": "rsw pos number",
    "summary": """
    - Change Receipt Number of POS to other format
    - Customize Receipt Report
    """,
    "author": "TienLD",
    "category": "Sales/Point Of Sale",
    "version": "13.0",
    "depends": ["point_of_sale"],
    "data": [
        # Views
        "views/pos_template.xml",
        "views/pos_order.xml",
    ],
    "qweb": ["static/src/xml/pos.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
}
