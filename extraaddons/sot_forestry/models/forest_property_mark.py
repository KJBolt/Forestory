# -*- coding: utf-8 -*-
# Part of School of Thought, Bangladesh and Geo Iworks, Ghana. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ForestPropertyMark(models.Model):
    _name = "forest.property.mark"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Property Mark"

    name = fields.Char(string="Name", required=True, tracking=True)
    set_type = fields.Selection([
        ('property_mark', 'Property Mark'),
        ('species', 'Species'),
        ('defect', 'Defect'),
        ('district', 'District'),
        ('costing', 'COSTING'),
        ('feedback', 'FEEDBACK'),
        ('overhead', 'OVERHEAD'),
        ('down_time', 'DOWN TIME'),
        ],
        string="Set Type",
        tracking=True,
    )
    active = fields.Boolean(string="Active", default=True)
    note = fields.Text(string="Description")
