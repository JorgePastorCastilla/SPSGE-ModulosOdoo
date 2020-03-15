from odoo import models, fields, api


class Racer(models.Model):
    _name = 'karting.racer'

    first_name = fields.Char('First name', size=30, required=True)
    last_name = fields.Char('Last name', size=40, required=True)

    name_complete = fields.Char(string='First Name with Last Name', compute='nom_complete')

    birthdate = fields.Date('Birthdate', required=True)
    phone = fields.Char('Phone', required=False)
    email = fields.Char('Email', required=False)
    address = fields.Char('Address', required=False)
    zip = fields.Char('Zip', required=False)
    city = fields.Char('City', required=False)

    state_id = fields.Many2one(comodel_name='res.country.state', string='State', required=False)
    country_id = fields.Many2one(comodel_name='res.country', string='Country', required=False)
    race_ids = fields.One2many('karting.diary.racer', 'racer_id', 'Races', readonly=True)


    active = fields.Boolean('Activate', default=True)

    @api.depends('first_name', 'last_name')
    def nom_complete(self):
        for x in self:
                    x.fullName = x.first_name + ' ' + x.last_name