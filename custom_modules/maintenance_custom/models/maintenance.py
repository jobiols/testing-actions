# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools


class MaintenanceEquipment(models.Model):
    _inherit = "maintenance.equipment"

    user_ids = fields.One2many(
        comodel_name="maintenance.users", inverse_name="maintenance_id", string="User"
    )


class MaintenanceUsers(models.Model):
    _name = "maintenance.users"
    _description = "Users Maintenance Equipment"

    name = fields.Char(string="Name")
    maintenance_id = fields.Many2one(
        comodel_name="maintenance.equipment", string="Equipment"
    )
