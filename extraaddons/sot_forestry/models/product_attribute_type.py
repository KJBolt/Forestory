# -*- coding: utf-8 -*-
# Part of School of Thought, Bangladesh and Geo Iworks, Ghana. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ProductAttributeType(models.Model):
    _name = 'product.attribute.type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Product Attribute Type'
    _order = 'id desc'

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Name")
    sequence = fields.Integer(string="Sequence", default=10, index=True)
    note = fields.Text(string="Note")
