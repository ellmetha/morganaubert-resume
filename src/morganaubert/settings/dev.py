# -*- coding: utf-8 -*-

# Standard library imports
# Third party imports
# Local application / specific library imports
from .base import *


DEBUG = True

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

ALLOWED_HOSTS = [
    'localhost:8000',
]

INTERNAL_IPS = (
    '127.0.0.1',
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
