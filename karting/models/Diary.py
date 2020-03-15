from odoo import models, fields, api


class Diary(models.Model):

    _name = 'karting.diary'

    name = fields.Char(string='Complex Date', compute='complex_date')

    date = fields.Date(string='Date', required=True)
    circuit_id = fields.Many2one(comodel_name='karting.circuit', string='Circuit', required=True)
    obs = fields.Text(string="Observations", required=False)
    racer_ids = fields.One2many(comodel_name='karting.diary.racer', inverse_name='diary_id', string='Racers', required=False)
    rounds_ids = fields.One2many(comodel_name='karting.round', inverse_name='diary_id', string='Round', required=False)

    active = fields.Boolean('Activate', default=True)

    @api.depends('date')
    def complex_date(self):
        for x in self:
                    x.name = x.date + ' ' + x.circuit_id.name
