# -*- coding: utf-8 -*-
{
    'name': "HR Attendance Geolocation",
    'version': '18.0.1.0.0',
    'summary': "Adds geolocation and work locations to attendances.",
    'license': 'LGPL-3',
    'author': "Tu Nombre o Empresa",
    'website': "https://www.tuweb.com",
    'category': 'Human Resources/Attendances',
    'depends': [
        'hr_attendance',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_work_location_views.xml',
        'views/hr_attendance_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'hr_attendance_geolocation/static/src/js/attendance_geolocation.js',
        ],
    },
    'installable': True,
}