from odoo import models, fields

class Formation(models.Model):
    _name = 'formation.formation'
    _description = 'Catalogue des formations'

    name = fields.Char(string="Nom de la formation", required=True)
    description = fields.Text(string="Description")
    categorie_id = fields.Many2one('formation.categorie', string="Catégorie")
    duree_estimee = fields.Integer(string="Durée estimée (heures)")
    session_ids = fields.One2many('formation.session', 'formation_id', string="Sessions")
    prix = fields.Float(string="Coût de la formation")
    image = fields.Binary("Image de la formation")
