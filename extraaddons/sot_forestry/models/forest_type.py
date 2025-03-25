# -*- coding: utf-8 -*-
# Part of School of Thought, Bangladesh and Geo Iworks, Ghana. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ForestType(models.Model):
    _name = 'forest.type'
    _description = 'Forest Type'
    _order = 'id desc'

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Name", required=True)
    sequence = fields.Integer(string="Sequence", default=10, index=True)
    note = fields.Text(string="Note")
