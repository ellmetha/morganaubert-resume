# -*- coding: utf-8 -*-

# Standard library imports
import json
import os

# Third party imports
from django.core.exceptions import ImproperlyConfigured

# Local application / specific library imports


# Secrets handling
# --------------------------------------

# JSON-based secrets module
with open(os.path.dirname(os.path.realpath(__file__)) + '/' + 'secrets.json') as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    """
    Get the secret variable or return explicit exception.
    """
    try:
        return secrets[setting]
    except KeyError:
        error_msg = 'Set the {0} environment variable'.format(setting)
        raise ImproperlyConfigured(error_msg)


# Django settings
# --------------------------------------

PROJECT_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../..')

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DOMAIN_NAME = 'morganaubert.fr'

ADMINS = (
    ('dev', get_secret('EMAIL_DEV')),
)

MANAGERS = (
    ('team', get_secret('EMAIL_TEAM')),
)

ALLOWED_HOSTS = [
    DOMAIN_NAME,
]


# The from: field in errors emails
SERVER_EMAIL = 'django-error@{}'.format(DOMAIN_NAME)
EMAIL_USE_TLS = True
EMAIL_HOST = get_secret('EMAIL_HOST')
EMAIL_HOST_USER = get_secret('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_secret('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('DB_USER'),
        'PASSWORD': get_secret('DB_PASSWORD'),
        'HOST': get_secret('DB_HOST'),
        'PORT': '',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr'

LANGUAGES = (
    ('en', 'English'),
)

LOCALE_PATHS = (
    os.path.join(PROJECT_PATH, 'src/morganaubert/locale'),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# URL of the admin page
ADMIN_URL = 'ma-admin/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'public/media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'http://media.{}/'.format(DOMAIN_NAME)

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, 'public/static/')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = 'http://static.{}/'.format(DOMAIN_NAME)

# Additional locations of static files
STATICFILES_DIRS = ()

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

# Make this unique, and don't share it with anybody.
SECRET_KEY = get_secret('SECRET_KEY')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'utils.context_processors.site',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'templates'),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
)

ROOT_URLCONF = 'morganaubert.urls'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'morganaubert.wsgi.application'

INSTALLED_APPS = (
    # Django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    # Third party apps
    'googletools',
    'pipeline',

    # Local apps
    'morganaubert',
)


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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


#  Debug toolbar settings
# --------------------------------------

# The debug toolbar patches the URL config when its models.py is loaded, which in turn triggers the plugin discovery to misbehave.
DEBUG_TOOLBAR_PATCH_SETTINGS = False


# Django pipeline settings
# --------------------------------------

PIPELINE_CSS = {
    'theme': {
        'source_filenames': (
            'less/theme.less',
            'less/print.less',
        ),
        'output_filename': 'css/theme.css',
    },

    'ie': {
        'source_filenames': (
            'less/ie.less',
        ),
        'output_filename': 'css/ie.css',
    },
}

PIPELINE_JS = {
    'libraries': {
        'source_filenames': (
            'js/vendor/jquery.js',
            'js/vendor/jquery.easing.js',
            'js/vendor/bootstrap/affix.js',
            'js/vendor/bootstrap/collapse.js',
            'js/vendor/bootstrap/dropdown.js',
            'js/vendor/bootstrap/modal.js',
            'js/vendor/bootstrap/tab.js',
            'js/vendor/bootstrap/tooltip.js',
            'js/vendor/bootstrap/transition.js',
        ),
        'output_filename': 'js/libraries.js',
    },

    'application': {
        'source_filenames': (
            'js/main.js',
        ),
        'output_filename': 'js/application.js'
    }
}

PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)
