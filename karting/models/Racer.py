from odoo import models, fields, api


class Racer(models.Model):
    _name = 'karting.racer'
    # name = fields.Char('Circuit')
    first_name = fields.Char('First name', size=30, required=True)
    last_name = fields.Char('Last name', size=40, required=True)
    birthdate = fields.Date('Birthdate', required=True)
    phone = fields.Char('Phone', required=False)
    email = fields.Char('Email', required=False)
    address = fields.Char('Address', required=False)
    zip = fields.Char('Zip', required=False)
    city = fields.Char('City', required=False)
    state_id = fields.Many2one(comodel_name='res.country.state', string='State', required=False)
    country_id = fields.Many2one(comodel_name='res.country', string='Country', required=False)
    race_ids = fields.Many2one('karting.diary.racer', 'racer_id', 'Races', readonly=True)
