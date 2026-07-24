from odoo import models, fields

class Employee(models.Model):
    _inherit = 'hr.employee'

    CURP = fields.Char(string='CURP')
    RFC = fields.Date(string='RFC')
    NSS = fields.Char(string='NSS')
    Est = fields.Char(string='Estatus')
