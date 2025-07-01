
from odoo import models ,fields ,api
from odoo.exceptions import ValidationError
from datetime import timedelta


class GymSubscription (models.Model):


        _name = 'gym.subscription'
        _description = 'Gym Subscription'
        _rec_name = 'member_id'

        member_id = fields.Many2one('gym.member', string='Member', required=True)
        trainer_id = fields.Many2one('gym.trainer', string='Trainer')
        available_days = fields.Many2many('gym.weekday',string='Trainer Available Days', compute='_compute_available_days',store=False)
        subscription_type = fields.Selection([
            ('monthly', 'Monthly'),
            ('quarterly', 'Quarterly'),
            ('yearly', 'Yearly')
        ], string='Subscription Type', required=True)
        start_date = fields.Date(string='Start Date', required=True, default=fields.Date.today)
        end_date = fields.Date(string='End Date', compute='_compute_end_date', store=True)
        price = fields.Float(string='Price', required=True)
        state = fields.Selection([
            ('active', 'Active'),
            ('expired', 'Expired')
        ], string='Status', default='active')
        duration = fields.Integer(string='Duration (Days)', compute='_compute_duration', store=True)

        @api.depends('start_date', 'subscription_type')
        def _compute_end_date(self):
            for record in self:
                if record.start_date and record.subscription_type:
                    if record.subscription_type == 'monthly':
                        record.end_date = record.start_date + timedelta(days=30)
                    elif record.subscription_type == 'quarterly':
                        record.end_date = record.start_date + timedelta(days=90)
                    elif record.subscription_type == 'yearly':
                        record.end_date = record.start_date + timedelta(days=365)
                else:
                    record.end_date = False

        @api.depends('start_date', 'end_date')
        def _compute_duration(self):
            for record in self:
                if record.start_date and record.end_date:
                    record.duration = (record.end_date - record.start_date).days
                else:
                    record.duration = 0

        @api.depends('trainer_id')
        def _compute_available_days(self):
            for record in self:
                if record.trainer_id:
                    record.available_days = record.trainer_id.available_days
                else:
                    record.available_days = [(5, 0, 0)]  # clear the field
