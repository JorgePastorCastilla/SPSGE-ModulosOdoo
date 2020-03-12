from odoo import models, fields, api

class Circuit(models.Model):
    # _inherit = 'libro.task'
    _name = 'karting.circuit'
    name = fields.Char('Circuit')

