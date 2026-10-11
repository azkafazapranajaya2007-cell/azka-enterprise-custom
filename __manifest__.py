{
    'name': 'Azka Enterprise Custom Theme & System',
    'version': '17.0.10.0.0',
    'category': 'Customizations',
    'summary': 'Zenith Edition - High-End Enterprise Branding & UI Architecture',
    'author': 'Azka Faza Pranajaya',
    'depends': ['base', 'web'],
    'data': [
        'views/web_title_views.xml',
        'views/login_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'azka_enterprise_custom/static/style.css',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
