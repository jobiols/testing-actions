def migrate(cr, version):
    cr.execute(""" UPDATE
            hr_employee
        SET
            ial = 1
        WHERE
            ial is NULL
    """)

    cr.execute(""" UPDATE
            hr_employee
        SET
            sal = 1
        WHERE
            sal is NULL
    """)
    cr.execute(""" UPDATE
            hr_employee
        SET
            nda_type = 'by_company'
        WHERE
            nda_type is NULL
    """)
