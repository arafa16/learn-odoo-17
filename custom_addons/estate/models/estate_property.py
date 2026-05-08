from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description", default="No description provided.")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available From", default=fields.Datetime.now)
    expected_price = fields.Float(string="Expected Price")
    selling_price = fields.Float(string="Selling Price", default=1000000)
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

