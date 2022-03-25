##############################################################################
#
#    Copyright (C) 2021  Quilsoft  (http://www.quilsoft.com)
#    All Rights Reserved.
#
##############################################################################

{
    "name": "hr_generic_custom",
    "version": "14.0.2.0.0",
    "category": "Tools",
    "summary": "Changes in employee fields",
    "author": "Quilsoft",
    "website": "http://github.com/quilsoft/cl-invaph",
    "license": "AGPL-3",
    "depends": [
        "hr",
        "l10n_nl_employee_extended",
    ],
    "data": [
        "views/hr_employee.xml",
        "security/ir.model.access.csv",
    ],
    "installable": True,
}
