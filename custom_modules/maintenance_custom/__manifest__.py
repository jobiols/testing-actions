##############################################################################
#
#    Copyright (C) 2021  Quilsoft  (http://www.quilsoft.com)
#    All Rights Reserved.
#
##############################################################################

{
    'name': 'Maintenance Custom',
    'version': '14.0.1.0.0',
    'category': 'hr',
    'summary': "Add fields maintenance module",
    'author': "Quilsoft",
    'website': 'http://github.com/quilsoft/cl-invaph',
    'license': 'AGPL-3',
    'depends': [
        'maintenance',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/maintenance_view.xml',
    ],
    'installable': True,

    'odoo-license': 'EE',

}
