from odoo import fields, models, api


class Round (models.Model):
    _name = 'karting.round'
    _description = 'Description'
    
    name = fields.Char(string='Time', required=False)
    diary_id = fields.Many2one(comodel_name='karting.diary', string='Diary', required=False)
    racer_ids = fields.One2many(comodel_name='karting.diary.racer', inverse_name='round_id', string='Racers', required=False, readonly=True)

    


