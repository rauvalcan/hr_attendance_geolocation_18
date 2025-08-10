# -*- coding: utf-8 -*-
from odoo import models, fields

class HrWorkLocation(models.Model):
    _name = 'hr.work.location'
    _description = 'Work Location'

    name = fields.Char(string='Location Name', required=True)
    address = fields.Text(string='Address')
    location_type = fields.Selection(
        [('onsite', 'On-Site'), ('remote', 'Remote')],
        string='Location Type', default='onsite', required=True
    )
    latitude = fields.Float(string='Latitude', digits=(10, 7))
    longitude = fields.Float(string='Longitude', digits=(10, 7))
    radius = fields.Float(string='Radius (meters)', default=100)