from odoo import models, fields, api
from datetime import date

class Session(models.Model):
    _name = 'formation.session'
    _description = 'Session de formation'

    name = fields.Char(string="Nom de la session", required=True)
    formation_id = fields.Many2one('formation.formation', string="Formation", required=True)
    date_debut = fields.Date(string="Date de début")
    date_fin = fields.Date(string="Date de fin")
    duree = fields.Integer(string="Durée (heures)")
    formateur_id = fields.Many2one('formation.formateur', string="Formateur")
    participant_ids = fields.Many2many('formation.participant', string="Participants")
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('confirmed', 'Confirmée'),
        ('done', 'Terminée'),
    ], string="Statut", default='draft')


    