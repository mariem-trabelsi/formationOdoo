from odoo import models, fields

class Formateur(models.Model):
    _name = 'formation.formateur'
    _description = 'Formateur'

    name = fields.Char(string="Nom", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Téléphone")
    expertise = fields.Text(string="Expertise")
    session_ids = fields.One2many('formation.session', 'formateur_id', string="Sessions animées")
