from odoo import models, fields, api
import json

class SkinConsultation(models.Model):
    _name = 'skin.consultation'
    _description = 'Skin Consultation'

    like_about_skin = fields.Text(string='Skin Likes', help='Array of skin attributes the customer likes')
    like_about_skin_display = fields.Char(string='Skin Likes', compute='_compute_like_about_skin_display')

    improve_about_skin = fields.Text(string='Skin Improvements', help='Array of skin attributes the customer wants to improve')
    improve_about_skin_display = fields.Char(string='Skin Improvements', compute='_compute_improve_about_skin_display')

    vascularity = fields.Selection([
        ('hypo', 'Hypo'),
        ('normal', 'Normal'),
        ('hyper', 'Hyper'),
        ('other', 'Other')
    ], string='Vascularity')
    skin_texture = fields.Selection([
        ('thin', 'Thin'),
        ('medium', 'Medium'),
        ('thick', 'Thick'),
        ('other', 'Other')
    ], string='Skin Texture')
    pigmentation = fields.Selection([
        ('superficial', 'Superficial'),
        ('dermal', 'Dermal'),
        ('both', 'Both'),
        ('other', 'Other')
    ], string='Depth of Pigmentation')
    hydration = fields.Selection([
        ('extreme_dehydrated', 'Extreme Dehydrated'),
        ('dehydrated', 'Dehydrated'),
        ('normal', 'Normal'),
        ('other', 'Other')
    ], string='Hydration Level')
    sebaceous_activity = fields.Selection([
        ('hypo', 'Hypo'),
        ('normal', 'Normal'),
        ('hyper', 'Hyper'),
        ('other', 'Other')
    ], string='Sebaceous Activity')


    @api.depends('like_about_skin')
    def _compute_like_about_skin_display(self):
        for record in self:
            if record.like_about_skin:
                try:
                    likes = json.loads(record.like_about_skin)
                    record.like_about_skin_display = ', '.join(likes)
                except:
                    record.like_about_skin_display = record.like_about_skin
            else:
                record.like_about_skin_display = ''

    @api.depends('improve_about_skin')
    def _compute_improve_about_skin_display(self):
        for record in self:
            if record.improve_about_skin:
                try:
                    improvements = json.loads(record.improve_about_skin)
                    record.improve_about_skin_display = ', '.join(improvements)
                except:
                    record.improve_about_skin_display = record.improve_about_skin
            else:
                record.improve_about_skin_display = ''
    