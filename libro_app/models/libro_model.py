#-*- coding: utf-8 -*-
from odoo import models, fields, api

class LibroTask(models.Model):
    _name = 'libro.task'
    name = fields.Char('Titulo', required=True)
    # titulo = fields.Char('Title', required=True)
    autor = fields.Char('Author')
    paginas = fields.Integer('Pages')
    editorial = fields.Char("Editorial")