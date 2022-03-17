##############################################################################
#
#    Copyright (C) 2021  Quilsoft  (http://www.quilsoft.com)
#    All Rights Reserved.
#
##############################################################################

{
    'name': 'Base custom',
    'version': '14.0.1.0.0',
    'category': 'Tools',
    'summary': "Translations",
    'author': "Quilsoft",
    'website': 'http://github.com/quilsoft/cl-invaph',
    'license': 'AGPL-3',
    'depends': [
        'analytic',
        'account',
    ],
    'data': [
        'views/res_partner_view.xml',
    ],
    'installable': True,
}
