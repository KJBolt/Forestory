{
    'name': 'Aloette',
    'category': 'Generic Modules/Human Resources',
    'author': 'GeoiWorks',
    'version': '17.0.1.0.2',
    'sequence': 3,
    'license': 'LGPL-3',
    'summary': 'Skin care management system for aloette',
    'description': """Skin care management system for aloette.""",
    'depends': ['web'],
    'data': [
        'views/skin_consultation_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'aloette/static/src/components/skin_consultation/skin_consultation.xml',
            'aloette/static/src/components/skin_consultation/skin_consultation.js',
            'aloette/static/src/components/skin_consultation/skin_consultation.scss',
        ],
    },
    'images': ['static/description/banner.png'],
    'application': True,
}
