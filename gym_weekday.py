from odoo import models ,fields ,api
from odoo.exceptions import ValidationError
from datetime import timedelta


class GymWeekday(models.Model):
    _name = 'gym.weekday'
    _description = 'Weekday'

    name = fields.Char(string='Day Name', required=True)
