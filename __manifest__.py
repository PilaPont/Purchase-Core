{
    'name': 'Purchase Core',
    'version': '14.0.0.1.1.1+210705',
    'description': """
     This module modifies some properties of Purchase, including:
            _ Convert original purchase demo and data records into Farsi
            _ Add monetary widget to price_unit
    """,
    'author': "Kenevist Developers, Maryam Kia",
    'website': "https://www.kenevist.ir",
    'license': 'OPL-1',
    'category': 'Localization',
    'depends': ['purchase'],
    'data': [
        'views/purchase_order_views.xml',
        'data/mail_template_data.xml',
        'data/purchase_data.xml',
        'report/purchase_order_templates.xml',
    ],
    'demo': [
        'data/purchase_demo.xml',
    ],
    'auto_install': True,
    'application': False,
    'installable': True,
}
