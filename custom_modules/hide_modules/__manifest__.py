##############################################################################
#
#    Copyright (C) 2021  Quilsoft  (http://www.quilsoft.com)
#    All Rights Reserved.
#
##############################################################################

{
    'name': 'Hide Modules',
    'version': '14.0.1.0.0',
    'category': 'Tools',
    'summary': "Hide discuss, calendary, contacts",
    'author': "Quilsoft",
    'website': 'http://github.com/quilsoft/cl-invaph',
    'license': 'AGPL-3',
    'depends': ['mail','contacts','calendar'],
    'data': [
        'views/hide_modules.xml'
    ],
    'installable': True,
}
