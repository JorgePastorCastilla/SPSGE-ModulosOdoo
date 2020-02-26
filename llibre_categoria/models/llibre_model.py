from odoo import models, fields, api

class Categoria(models.Model):
    _name = 'libro.categoria'
    name = fields.Char('Nombre Categoria')

class Llibre(models.Model):
    _inherit = 'libro.task'
    isbn = fields.Char('Isbn')
    precio = fields.Float('Precio')
    resumen = fields.Text('Resumen')
    fecha = fields.Date('Fecha')
    revisado = fields.Boolean('Revisado')
    aprobado = fields.Selection([('si', 'Si'), ('no', 'No'), ('pendiente', 'Pendiente')])
    categoria = fields.Many2one('libro.categoria','Categoria')

