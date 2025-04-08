from odoo import models, fields

class Categorie(models.Model):
    _name = 'formation.categorie'
    _description = 'Catégorie de formation'

    name = fields.Char(string="Nom", required=True)
    description = fields.Text(string="Description")
    formation_ids = fields.One2many('formation.formation', 'categorie_id', string="Formations")
