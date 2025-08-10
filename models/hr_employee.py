# -*- coding: utf-8 -*-
from odoo import models, api
import math

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    def _attendance_action_change(self):
        res = super()._attendance_action_change()
        latitude = self.env.context.get("latitude")
        longitude = self.env.context.get("longitude")

        if res and latitude and longitude:
            vals = {}
            if self.attendance_state == "checked_in":
                vals.update({
                    "check_in_latitude": latitude,
                    "check_in_longitude": longitude,
                })
                work_location = self._get_work_location_from_gps(latitude, longitude)
                if work_location:
                    vals["work_location_id"] = work_location.id
            else:
                vals.update({
                    "check_out_latitude": latitude,
                    "check_out_longitude": longitude,
                })
            res.write(vals)
        return res

    def _get_work_location_from_gps(self, latitude, longitude):
        locations = self.env['hr.work.location'].search([('location_type', '=', 'onsite')])
        for loc in locations:
            if loc.latitude and loc.longitude:
                R = 6371000  # Radio de la Tierra en metros
                lat1_rad, lon1_rad = math.radians(latitude), math.radians(longitude)
                lat2_rad, lon2_rad = math.radians(loc.latitude), math.radians(loc.longitude)
                dlon, dlat = lon2_rad - lon1_rad, lat2_rad - lat1_rad
                a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
                c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
                distance = R * c
                if distance <= loc.radius:
                    return loc
        return self.env['hr.work.location']