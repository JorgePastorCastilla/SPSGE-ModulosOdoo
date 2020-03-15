from odoo import fields, models, api

from dateutil import relativedelta
from dateutil import parser

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
    birthday = fields.Date(compute='birthday_method', string='Birthday', store=True)

    def isAdult(self):
        for test in self:
            if str(parser.parse(test.diary_id.date) - relativedelta.relativedelta(years=18)) >= test.racer_id.birthdate:
                return True
            else:
                return False

    def birthday_method(self):
        for x in self:
            for y in x.racer_id:
                return y.birthdate