from odoo import fields, models, api


class Karting_kart_type (models.Model):
    _name = 'karting.kart_type'
    _description = 'Description'
    name = fields.Char(string='Type', size=30,required=True)
    cilinder = fields.Integer(string='Cilinder Capacity (cc)', required=False)
    


