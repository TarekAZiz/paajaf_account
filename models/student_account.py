# -*- coding: utf-8 -*-

from odoo import models, fields, api

class student_account(models.Model):
    _inherit = "account.invoice"
    student_name = fields.Char("student.name")

#    self.env.cr.execute("""Select name from student_student""") 
#   results = self.env.cr.dictfetchall()
    student_code = fields.Char("student.code")
    standard_id = fields.Char("student.standard_id")
   
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
