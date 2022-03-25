from xml.etree.ElementTree import QName
from odoo import fields, models, api


class HRScreningLevel(models.Model):
    _name = "hr.screning.level"
    _description = "Screening level model"

    screnning_level = fields.Selection(
        [
            ("not_available", "Not Available yet"),
            ("vog", "VOG"),
            ("cap", "CAP"),
            ("vgbb", "VGBB"),
        ],
        required=True,
    )
    expire_screning_level = fields.Date(string="Screning level Expiry", required=True)
    employee_id = fields.Many2one("hr.employee")


class HREmployeeGeneric(models.Model):
    _inherit = "hr.employee"
    _description = "Employee Extension"

    ial = fields.Selection(
        [
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("5", "5"),
            ("6", "6"),
            ("7", "7"),
            ("8", "8"),
            ("9", "9"),
            ("10", "10"),
            ("11", "11"),
        ],
        string="IAL",
        required=True,
    )
    sal = fields.Selection(
        [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4")], string="SAL", required=True
    )
    nda_signed = fields.Boolean(string="NDA Signed", default=False)
    nda_type = fields.Selection(
        [("by_company", "By Company"), ("individual", "Individual")],
        string="NDA Type",
        required=True,
    )
    screning_level_ids = fields.One2many(
        "hr.screning.level", "employee_id", string="Screning level"
    )
