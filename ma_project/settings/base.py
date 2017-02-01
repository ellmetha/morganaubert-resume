"""
    Base Django settings for morganaubert-resume project
    ====================================================

    For more information on this file, see https://docs.djangoproject.com/en/dev/topics/settings/
    For the full list of settings and their values, see
    https://docs.djangoproject.com/en/dev/ref/settings/
"""

import json
import pathlib
import os

from django.core.exceptions import ImproperlyConfigured

PROJECT_PATH = pathlib.Path(__file__).parents[2]


# ENVIRONMENT SETTINGS HANDLING
# ------------------------------------------------------------------------------

ENVSETTINGS_FILENAME = '.env.json'
ENVSETTINGS_NIL = object()

# JSON-based environment module
with open(os.environ.get('ENVSETTINGS_FILEPATH') or str(PROJECT_PATH / ENVSETTINGS_FILENAME)) as f:
    secrets = json.loads(f.read())


def get_envsetting(setting, default=ENVSETTINGS_NIL, secrets=secrets):
    """ Get the environment setting variable or return explicit exception. """
    try:
        return secrets[setting]
    except KeyError:
        if default is not ENVSETTINGS_NIL:
            return default
        error_msg = 'Set the {} environment variable in the {} file'.format(
            setting, ENVSETTINGS_FILENAME)
        raise ImproperlyConfigured(error_msg)


# APP CONFIGURATION
# ------------------------------------------------------------------------------

INSTALLED_APPS = (
    # Django apps
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',

    # Third party apps
    'meta',

    # Local apps
    'ma',
)


# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


# DEBUG CONFIGURATION
# ------------------------------------------------------------------------------

# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------

# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': get_envsetting('DB_ENGINE'),
        'NAME': get_envsetting('DB_NAME'),
        'USER': get_envsetting('DB_USER'),
        'PASSWORD': get_envsetting('DB_PASSWORD'),
        'HOST': get_envsetting('DB_HOST'),
        'PORT': get_envsetting('DB_PORT', ''),
        'OPTIONS': get_envsetting('DB_OPTIONS'),
    }
}


# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'EST'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en'

# See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
DOMAIN_NAME = 'morganaubert.name'
ALLOWED_HOSTS = [
    DOMAIN_NAME,
    'www.{}'.format(DOMAIN_NAME),
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#languages
LANGUAGES = (
    ('en', 'English'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = (
    str(PROJECT_PATH / 'ma_project' / 'locale'),
)

ADMINS = (
    ('dev', get_envsetting('EMAIL_DEV')),
)

MANAGERS = (
    ('team', get_envsetting('EMAIL_TEAM')),
)


# SECRET CONFIGURATION
# ------------------------------------------------------------------------------

# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_envsetting('SECRET_KEY')


# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------

# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (
            str(PROJECT_PATH / 'ma' / 'templates'),
        ),
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'ma_project.context_processors.google_metadata',
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', (
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                )),
            ]
        },
    },
]


# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(PROJECT_PATH / 'public' / 'static')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    str(PROJECT_PATH / 'ma' / 'static' / 'build'),
    str(PROJECT_PATH / 'ma' / 'static'),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-STATICFILES_STORAGE
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'


# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(PROJECT_PATH / 'public' / 'media')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'


# URL CONFIGURATION
# ------------------------------------------------------------------------------

ROOT_URLCONF = 'ma_project.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'ma_project.wsgi.application'


# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------

# See: http://docs.djangoproject.com/en/dev/topics/logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['console'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}


# GOOGLE CONFIGURATION
# ------------------------------------------------------------------------------

GOOGLE_SITE_VERIFICATION_CODE = get_envsetting('GOOGLE_SITE_VERIFICATION_CODE')
