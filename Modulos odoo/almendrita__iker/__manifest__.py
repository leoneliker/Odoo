# -*- coding: utf-8 -*-
{
    'name': "Almendrita_Iker",

    'summary': """
            Nuevo modulo para el "examen"
        """,

    'description': """
        Este es el nuevo modulo que me han pedido desarrollar en el "examen" de SGE
    """,

    'author': "Iker Iturralde",
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
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application' : True
}
