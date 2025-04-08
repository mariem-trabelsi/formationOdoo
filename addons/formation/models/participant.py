from odoo import models, fields

class Participant(models.Model):
    _name = 'formation.participant'
    _description = 'Participant à une formation'

    name = fields.Char(string="Nom", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Téléphone")
    company_id = fields.Many2one('res.partner', string="Entreprise")
    session_ids = fields.Many2many('formation.session', string="Sessions suivies")
