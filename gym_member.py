from odoo import models ,fields ,api
from odoo.exceptions import ValidationError



class GymMember (models.Model):
     _name ="gym.member"
     name = fields.Char()
     age= fields.Char()
     phone = fields.Char(size =11)
     start_date = fields.Date()
     image = fields.Binary()
     subscription_duration = fields.Integer(string='Duration (Days)', compute='_compute_duration', store=True)

     subscription_type = fields.Selection([
         ('monthly', 'Monthly'),
         ('quarterly', 'Quarterly'),
         ('yearly', 'Yearly')

         ])


     status = fields.Selection([
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('suspended', 'Suspended')
          ], string='Subscription Status', default='active')

     _sql_constraints = [ ('unique_phone', 'unique(phone)', 'Phone number must be unique!')]

     @api.depends('subscription_type')
     def _compute_duration(self):
         for rec in self:
             if rec.subscription_type == 'monthly':
                 rec.subscription_duration = 30
             elif rec.subscription_type == 'quarterly':
                 rec.subscription_duration = 90
             elif rec.subscription_type == 'yearly':
                    rec.subscription_duration = 365

# # id(PK), name, age, gender, phone, phone, membership_plan_id(FK), start_date, end_date, active
#      @api.onchange('start_date','end_date' )
#      def check_end_date(self):
#        end_date_ids = self.search([])
#        for rec in end_date_ids:
#          if rec.start_date and rec.end_date < fields.date.today():
#             rec.is_late = True
#
#          else:
#              rec.is_late = False