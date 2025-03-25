# -*- coding: utf-8 -*-
# Part of School of Thought, Bangladesh and Geo Iworks, Ghana. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ForestReverseCertificateStatus(models.Model):
    _name = "certificate.status"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Certificate Status"

    name = fields.Char(string="Name", required=True, tracking=True)
    sequence = fields.Integer(string='Sequence', default=10)
    active = fields.Boolean(string="Active", default=True)
    note = fields.Text(string="Note")
