{
    'name': 'Custom Logo',
    'version': '1.0',
    'category': 'Customization',
    'summary': 'Custom Logo and Favicon for Odoo',
    'description': 'This module replaces the default Odoo logo and favicon with custom images.',
    'author': 'OXORDPH',
    'website': 'https://github.com/OXORDPH/Computer-Solutions-Repair-Center',
    'license': 'LGPL-3',
    'depends': ['web'],
    'data': [],
    'assets': {
        'web.assets_backend': [
            'custom_logo/static/src/img/oxord-icon-512x512.png',
            'custom_logo/static/src/img/favicon.ico',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}
