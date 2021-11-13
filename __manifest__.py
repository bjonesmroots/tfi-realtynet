# -*- coding: utf-8 -*-
{
    'name': "Realty.Net",

    'summary': """
        TFI - Parcial - Realty.Net CU1""",

    'description': """
        TFI - Parcial - Realty.Net CU1
    """,

    'author': "Brian Jones",
    'website': "https://www.mentalroots.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'data/planes.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}