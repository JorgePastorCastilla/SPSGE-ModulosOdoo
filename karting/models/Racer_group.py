from odoo import fields, models, api


class Racer_group (models.Model):
    _name = 'karting.racer.group'
    _description = 'Description'
    name = fields.Char(string='Name', required=False)
    racer_ids = fields.One2many(comodel_name='karting.diary.racer', inverse_name='group_id', string='Racers', required=False)
    


