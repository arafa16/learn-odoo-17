from odoo import models, fields, api
from odoo.exceptions import ValidationError

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    _sql_constraints = [
        (
            'unique_name',
            'UNIQUE(name)',
            'The property name must be unique.'
        )
    ]

    @api.constrains('selling_price')
    def _check_selling_price(self):
        for record in self:
            if record.selling_price < 1:
                raise ValidationError("Selling price cannot be negative or 0.")

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description", default="No description provided.")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available From", default=fields.Datetime.now)
    expected_price = fields.Float(string="Expected Price")
    selling_price = fields.Float(default=1000000)
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden_orientation = fields.Selection(
        string="Garden Orientation",
        selection=[("N", "North"), ("S", "South"), ("E", "East"), ("W", "West")],
    )
    last_seen = fields.Datetime(string="Last Seen", default=fields.Datetime.now)

