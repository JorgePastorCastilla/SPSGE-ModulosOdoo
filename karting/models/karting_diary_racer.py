from odoo import fields, models, api


class Karting_diary_racer(models.Model):
    _name = 'karting.diary.racer'
    _description = 'Description'

    racer_id = fields.Many2one(comodel_name='karting.racer', string='Racer', required=True)
    diary_id = fields.Many2one(comodel_name='karting.diary', string='Diary', required=True)
    kart_type = fields.Many2one(comodel_name='karting.kart_type', string='Type of kart', required=True)
    group_id = fields.Many2one(comodel_name='karting.racer.group', string='Group', required=False)
    turtor = fields.Char(string='Turtor', required=False, size=40)
    tutor_doc = fields.Char(string="Tutor's doc.", required=False, size=40)
    round_id = fields.Many2one(comodel_name='karting.round', string='Round', required=False)


