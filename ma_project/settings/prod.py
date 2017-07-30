"""
    Production Django settings for morganaubert-resume project
    ==========================================================

    This files imports the `base` settings and can add or modify previously defined settings to
    alter the configuration of the application for production environments.

    For more information on this file, see https://docs.djangoproject.com/en/dev/topics/settings/
    For the full list of settings and their values, see
    https://docs.djangoproject.com/en/dev/ref/settings/

"""

from .base import *  # noqa


# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------


MIDDLEWARE += ('django.middleware.security.SecurityMiddleware', )  # noqa: F405


# SECURITY CONFIGURATION
# ------------------------------------------------------------------------------

# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SECURE_HSTS_SECONDS
SECURE_HSTS_SECONDS = 31536000

# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SECURE_HSTS_INCLUDE_SUBDOMAINS  # noqa
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
