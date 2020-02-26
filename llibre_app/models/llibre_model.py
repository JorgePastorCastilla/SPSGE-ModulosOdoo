from odoo import models, fields, api

class Llibre(models.Model):
    _name = 'llibres'
    # paquito=fields.Integer('prueba primary key', primaryKey=True)
    name = fields.Char('Title', required=True)
    autor = fields.Char('Author of the book', required=True)
    paginas = fields.Integer('Number of pages', default=0)
    editorial = fields.Char('Editorial of the book')
    @api.one
    def do_toggle_done(self):
        self.is_done = not self.is_done
        return True

    @api.multi
    def do_clear_done(self):
        done_recs = self.search([('is_done', '=', True)])
        done_recs.write({'active': False})
        return True