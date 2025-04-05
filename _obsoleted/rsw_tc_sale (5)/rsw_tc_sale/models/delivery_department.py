from odoo import fields, models


class DeliveryDepartment(models.Model):
    _name = "delivery.department"
    _description = "Deliver to Department"

    # name = fields.Char("Department")
    name = fields.Selection([('dimsum','Dim Sum'),('hotpot','Hot Pot'),],'Deliver to Department',Default='dimsum')