from odoo import api, fields, models

class Contract(models.Model):
    _name = 'mrp.contract'
    _description = 'Contracts'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    contract_no = fields.Char(string="Contract No", required="True")
    buyer_name = fields.Char(string="Buyer Name", required=True)
    representative = fields.Many2one('res.partner', string="Representative", required="True")
    phone_no = fields.Char(string="Phone No", required="True")
    price = fields.Float(string="Price", required="True")
    email = fields.Char(string="Email", required="True")
    date = fields.Date(string="Date", required="True")
    specification_no = fields.Char(string="Specification No", required="True")
    delivery_start_date = fields.Date(string="Delivery Start Date", required="True")
    delivery_end_date = fields.Date(string="Delivery End Date", required="True")
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ], string="Status", default='new')
    
