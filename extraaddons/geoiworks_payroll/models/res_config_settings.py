# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_geoiworks_payroll_account = fields.Boolean(string='Payroll Accounting')

