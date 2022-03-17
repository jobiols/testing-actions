Hr generic custom
============

This module:
    - Create the Hr Screning Level models
    - Add the follow fields to Hr employee:
        - ial
        - sal
        - nda_signed
        - nda_type
        - screning_level_ids


# Release 0.0.11 - 2022-01-28

- Correccion de bug en una base existente no se puede instalar el módulo porque
falla al querer agregar constraints a los campos ial, sal y nda_type. Se aplica una
migracion para inicializar los campos antes de aplicar la constraint.
