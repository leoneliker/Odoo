# -*- coding: utf-8 -*-
{
    'name': "Gestion de garaje",

    'summary': """
        Gestión de colecciones de coches, no hay niños prometido.""",

    'description': """
        Este es un modulo de pruebas que trata acerca de como construir un modulo de odoo-14, realizado con cariño por Iker Iturralde y Joaquin Ayllón
    """,

    'author': "Iker Ayllon",
    'website': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/garaje_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/garaje_aparcamiento_report.xml',
        'data/garaje_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True
}
