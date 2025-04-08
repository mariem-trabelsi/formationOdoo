# -*- coding: utf-8 -*-
{
    'name': "formation",

    'summary': "Gestion des foramtions au sein de l'entreprisee",

    'description': """
Long description of module's purpose
    """,

    'author': "Mariem Trabelsi",
    'website': "https://www.meriem.tarbelsi.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'RH',
    'version': '0.1',

   
    'depends': ['base','web'],

  
    'data': [
        
        'security/formation_groups.xml',
        'security/ir.model.access.csv',
        'views/formation_views.xml',
        'views/session_views.xml',
        'views/participant_views.xml',
        'views/formateur_views.xml',
        'views/categorie_views.xml',
    ],
   
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}

