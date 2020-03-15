from odoo import  models, fields, api

from dateutil import relativedelta
import time
from dateutil import parser

class Circuit(models.Model):
    # _inherit = 'libro.task'
    _name = 'karting.circuit'
    name = fields.Char('Circuit')

class Diary(models.Model):

    _name = 'karting.diary'

    name = fields.Char(string='Complex Date', compute='complex_date')

    date = fields.Date(string='Date', required=True)
    circuit_id = fields.Many2one(comodel_name='karting.circuit', string='Circuit', required=True)
    obs = fields.Text(string="Observations", required=False)
    racer_ids = fields.One2many(comodel_name='karting.diary.racer', inverse_name='diary_id', string='Racers', required=False)
    round_ids = fields.One2many(comodel_name='karting.round', inverse_name='diary_id', string='Round', required=False)

    active = fields.Boolean('Activate', default=True)

    @api.depends('date')
    def complex_date(self):
        for x in self:
                    x.name = x.date + ' ' + x.circuit_id.name

class Kart_type (models.Model):
    _name = 'karting.kart_type'
    _description = 'Description'
    name = fields.Char(string='Type', size=30, required=True)
    cilinder = fields.Integer(string='Cilinder Capacity (cc)', required=False)


class Racer_group(models.Model):
    _name = 'karting.racer.group'
    _description = 'Description'
    name = fields.Char(string='Name', required=False)
    racer_ids = fields.One2many(comodel_name='karting.diary.racer', inverse_name='group_id', string='Racers', required=False)


class Round(models.Model):
    _name = 'karting.round'
    _description = 'Description'

    # name = fields.Char(string='Time', required=False)
    name = fields.Char(compute='complex_name', string='Round', store=True)
    time = fields.Float('Start')
    diary_id = fields.Many2one(comodel_name='karting.diary', string='Diary', required=False)
    racer_ids = fields.One2many(comodel_name='karting.diary.racer', inverse_name='round_id', string='Racers', required=False, readonly=True)

    @api.depends('diary_id')
    def complex_name(self):
        for x in self:
            prueba = "Circuito: " + x.diary_id.name
            x.name = ("Tiempo: ", "%02d:%02d" % (int(x.tiempo), (x.tiempo - int(x.tiempo)) * 60), prueba)

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
    race_ids = fields.Many2one('karting.diary.racer', 'racer_id', 'Races', readonly=True)

    active = fields.Boolean('Activate', default=True)

    @api.depends('first_name', 'last_name')
    def nom_complete(self):
        for x in self:
                    x.fullName = x.first_name + ' ' + x.last_name

class Diary_racer(models.Model):
    _name = 'karting.diary.racer'
    _description = 'Description'

    racer_id = fields.Many2one(comodel_name='karting.racer', string='Racer', required=True)
    diary_id = fields.Many2one(comodel_name='karting.diary', string='Diary', required=True)
    kart_type_id = fields.Many2one(comodel_name='karting.kart_type', string='Type of kart', required=True)
    group_id = fields.Many2one(comodel_name='karting.racer.group', string='Group', required=False)
    tutor = fields.Char(string='Tutor', required=False, size=40)
    tutor_doc = fields.Char(string="Tutor's doc.", required=False, size=40)
    round_id = fields.Many2one(comodel_name='karting.round', string='Round', required=False)

    mayoria_edad = fields.Boolean(compute='isAdult', string='Age', default=False)
    birthday = fields.Date(compute='birthday', string='Birthday', store=True)

    def isAdult(self):
        for test in self:
            if str(parser.parse(test.diary_id.date) - relativedelta.relativedelta(years=18)) >= test.racer_id.birthdate:
                return True
            else:
                return False

    def birthday(self):
        for x in self:
            for y in x.racer_id:
                return y.birthdate

