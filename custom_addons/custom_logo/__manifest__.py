{
    'name': 'oxordlogo',
    'version': '1.0',
    'category': 'Customization',
    'summary': 'Custom Logo and Favicon for Odoo',
    'description': 'This module replaces the default Odoo logo and favicon with custom images.',
    'author': 'OXORDPH',
    'website': 'https://oxordph-computer-solutions-repair-center.odoo.com/',
    'license': 'LGPL-3',
    'depends': ['web'],
    'data': [
    'views/assets.xml',
],
    'assets': {
        'web.assets_backend': [
            '/custom_logo/static/src/img/oxord-icon-512x512.png',
            '/custom_logo/static/src/img/favicon.ico',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,

    
}
