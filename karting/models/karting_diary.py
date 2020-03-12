from odoo import models, fields, api


class Karting_racer(models.Model):
    # _inherit = 'libro.task'
    _name = 'karting.diary'
    date = fields.Date(string='Date', required=True)
    circuit_id = fields.Many2one(comodel_name='karting.circuit', string='Circuit', required=True)
    obs = fields.Text(string="Observations", required=False)
    racer_ids = fields.One2many(comodel_name='karting.diary.racer', inverse_name='diary_id', string='Racers', required=False)
    round_ids = fields.One2many(comodel_name='karting.round', inverse_name='diary_id', string='Round', required=False)