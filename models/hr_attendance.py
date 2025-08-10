# -*- coding: utf-8 -*-
from odoo import models, fields

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    check_in_latitude = fields.Float(string='Check-in Latitude', digits=(10, 7), readonly=True)
    check_in_longitude = fields.Float(string='Check-in Longitude', digits=(10, 7), readonly=True)
    check_out_latitude = fields.Float(string='Check-out Latitude', digits=(10, 7), readonly=True)
    check_out_longitude = fields.Float(string='Check-out Longitude', digits=(10, 7), readonly=True)
    work_location_id = fields.Many2one(
        'hr.work.location', string='Work Location', readonly=True
    )