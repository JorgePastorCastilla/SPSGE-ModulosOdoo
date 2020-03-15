from odoo import fields, models, api


class Round (models.Model):
    _name = 'karting.round'
    _description = 'Description'
    
    # name = fields.Char(string='Time', required=False)
    name = fields.Char(compute='complex_name', string='Round', store=True)
    time = fields.Float('Start')
    diary_id = fields.Many2one(comodel_name='karting.diary', string='Diary', required=False)
    racer_ids = fields.One2many(comodel_name='karting.diary.racer', inverse_name='round_id', string='Racers', required=False)

    @api.depends('diary_id')
    def complex_name(self):
        for x in self:
            prueba = "Circuito: " + x.diary_id.name
            x.name = ("Tiempo: ", "%02d:%02d" % (int(x.tiempo), (x.tiempo - int(x.tiempo)) * 60), prueba)



