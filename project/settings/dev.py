# -*- coding: utf-8 -*-

from .base import *  # noqa


DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]

INTERNAL_IPS = (
    '127.0.0.1',
)

STATICFILES_DIRS = (
    str(PROJECT_PATH / 'static' / 'build_dev'),
    str(PROJECT_PATH / 'static' / 'build'),
    str(PROJECT_PATH / 'static'),
)

TEMPLATES[0]['OPTIONS']['loaders'] = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATES[0]['OPTIONS']['context_processors'] += (
    'project.context_processors.webpack',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += (
    'debug_toolbar',
)


LOGGING['loggers'] = {
    'django.request': {
        'handlers': ['console'],
        'level': 'ERROR',
        'propagate': True,
    },
}

WEBPACK_DEV_SERVER_URL = 'http://localhost:8080'
