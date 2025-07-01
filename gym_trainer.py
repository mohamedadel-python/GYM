from odoo import models ,fields ,api
from odoo.exceptions import ValidationError



class GymTrainer (models.Model):
     _name ="gym.trainer"
     name = fields.Char()
     age= fields.Char()
     phone = fields.Char(size =11)
     image = fields.Binary()
     available_days = fields.Many2many('gym.weekday', string='Available Days')

     _sql_constraints = [ ('unique_phone', 'unique(phone)', 'Phone number must be unique!')]

