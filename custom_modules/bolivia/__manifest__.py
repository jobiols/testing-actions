##############################################################################
#
#    Copyright (C) 2022  Quilsoft  (http://www.quilsoft.com)
#    All Rights Reserved.
#
##############################################################################

{
    'name': 'bolivia',
    'version': '14.0.1.0.0',
    'category': 'Tools',
    'summary': "Proyect module for Invap Bolivia",
    'author': "Quilsoft",
    'website': 'http://github.com/quilsoft/cl-invapb',
    'license': 'AGPL-3',
    'depends': [
        'account_accountant',
        'account',
        'l10n_bo',
        'sale',
        'sale_management',
        'purchase',
        'project',
        'sale_timesheet',
        'timesheet_grid',
        'stock',
        'hr',
        'hr_attendance',
        'hr_holidays',
        'hr_expense',
        'web_studio',
        'approvals',
        'calendar',
        'ks_dashboard_ninja',

        # desarrollados
        'base_custom',
        # 'employee_extend',
        'hide_modules',


        # Terceros
        'advanced_session_management',
        'auth_oauth_keycloak',
        'auto_backup',
    ],
    'installable': True,
}
