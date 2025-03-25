# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Odoofy Web Responsive',
    'category': 'Hidden',
    'version': '1.0',
   'author': 'odoofy',
    'website': 'https://odoofy.com',
    'description': """

        """,
    'depends': ['web', 'base_setup'],
    'auto_install': ['web'],
    'data': [
        'views/webclient_templates.xml',
    ],
    'icon': 'ofy_web_responsive/static/img/icon.png',
    'assets': {
        'web._assets_primary_variables': [
            ('after', 'web/static/src/scss/primary_variables.scss', 'ofy_web_responsive/static/src/**/*.variables.scss'),
            ('before', 'web/static/src/scss/primary_variables.scss', 'ofy_web_responsive/static/src/scss/primary_variables.scss'),
        ],
        'web._assets_secondary_variables': [
            ('before', 'web/static/src/scss/secondary_variables.scss', 'ofy_web_responsive/static/src/scss/secondary_variables.scss'),
        ],
        'web._assets_backend_helpers': [
            ('before', 'web/static/src/scss/bootstrap_overridden.scss', 'ofy_web_responsive/static/src/scss/bootstrap_overridden.scss'),
        ],
        'web.assets_frontend': [
            'ofy_web_responsive/static/src/webclient/home_menu/home_menu_background.scss', # used by login page
            'ofy_web_responsive/static/src/webclient/navbar/navbar.scss',
        ],
        'web.assets_backend': [
            'ofy_web_responsive/static/src/webclient/**/*.scss',
            'ofy_web_responsive/static/src/views/**/*.scss',

            'ofy_web_responsive/static/src/core/**/*',
            'ofy_web_responsive/static/src/webclient/**/*.js',
            'ofy_web_responsive/static/src/webclient/**/*.xml',
            'ofy_web_responsive/static/src/views/**/*.js',
            'ofy_web_responsive/static/src/views/**/*.xml',

            # Don't include dark mode files in light mode
            ('remove', 'ofy_web_responsive/static/src/**/*.dark.scss'),
        ],
        'web.assets_web': [
            ('replace', 'web/static/src/main.js', 'ofy_web_responsive/static/src/main.js'),
        ],
        # ========= Dark Mode =========
        "web.dark_mode_variables": [
            # web._assets_primary_variables
            ('before', 'ofy_web_responsive/static/src/scss/primary_variables.scss', 'ofy_web_responsive/static/src/scss/primary_variables.dark.scss'),
            ('before', 'ofy_web_responsive/static/src/**/*.variables.scss', 'ofy_web_responsive/static/src/**/*.variables.dark.scss'),
            # web._assets_secondary_variables
            ('before', 'ofy_web_responsive/static/src/scss/secondary_variables.scss', 'ofy_web_responsive/static/src/scss/secondary_variables.dark.scss'),
        ],
        "web.assets_web_dark": [
            ('include', 'web.dark_mode_variables'),
            # web._assets_backend_helpers
            ('before', 'ofy_web_responsive/static/src/scss/bootstrap_overridden.scss', 'ofy_web_responsive/static/src/scss/bootstrap_overridden.dark.scss'),
            ('after', 'web/static/lib/bootstrap/scss/_functions.scss', 'ofy_web_responsive/static/src/scss/bs_functions_overridden.dark.scss'),
            # assets_backend
            'ofy_web_responsive/static/src/**/*.dark.scss',
        ],
        'web.tests_assets': [
            'ofy_web_responsive/static/tests/*.js',
        ],
        'web.qunit_suite_tests': [
            'ofy_web_responsive/static/tests/views/**/*.js',
            'ofy_web_responsive/static/tests/webclient/**/*.js',
            ('remove', 'ofy_web_responsive/static/tests/webclient/action_manager_mobile_tests.js'),
        ],
        'web.qunit_mobile_suite_tests': [
            'ofy_web_responsive/static/tests/views/disable_patch.js',
            'ofy_web_responsive/static/tests/mobile/**/*.js',
            'ofy_web_responsive/static/tests/webclient/action_manager_mobile_tests.js',
        ],
    },
    'license': 'OPL-1',
}
