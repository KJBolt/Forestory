# -*- coding: utf-8 -*-
# Part of School of Thought, Bangladesh and Geo Iworks, Ghana. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class MachineMachine(models.Model):
    _name = "machine.machine"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Machine Machine"
    _order = 'id desc'

    name = fields.Char(string="Machine Name", tracking=True, required=True)
    sequence = fields.Integer(string="Sequence", default=10, index=True)
    active = fields.Boolean(string="Active", default=True)
    note = fields.Text(string="Note")
