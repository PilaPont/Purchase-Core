{
    'name': 'Purchase Core',
    'version': '14.0.0.1.2.0+210613',
    'description': """
     This module modifies some properties of Purchase, including:
    - Converts original CRM demo and data records into Farsi.
    """,
    'author': "Kenevist Developers, Maryam Kia",
    'website': "https://www.kenevist.ir",
    'license': 'OPL-1',
    'category': 'Localization',
    'depends': ['purchase'],
    'data': [
        'data/mail_template_data.xml',
        'data/purchase_data.xml',
    ],
    'demo': [
        'data/purchase_demo.xml',
    ],
    'auto_install': True,
    'application': False,
    'installable': True,
}
