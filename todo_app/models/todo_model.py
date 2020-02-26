from odoo import models, fields, api

class TodoTask(models.Model):
    _name = 'todo.task'
    # paquito=fields.Integer('prueba primary key', primaryKey=True)
    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)
    @api.one
    def do_toggle_done(self):
        self.is_done = not self.is_done
        return True

    @api.multi
    def do_clear_done(self):
        done_recs = self.search([('is_done', '=', True)])
        done_recs.write({'active': False})
        return True