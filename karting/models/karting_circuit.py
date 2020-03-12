from odoo import models, fields, api

class Karting_circuit(models.Model):
    # _inherit = 'libro.task'
    _name = 'karting.circuit'
    name = fields.Char('Circuit')

