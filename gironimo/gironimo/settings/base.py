import os
from unipath import Path

from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)


gettext_noop = lambda s: s

PROJECT_DIR = Path(__file__).ancestor(3)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Marc Rochow', 'mrochow@gironimo.org'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = ['.gironimo.org']

TIME_ZONE = 'Europe/Berlin'

LANGUAGE_CODE = 'de'

LANGUAGES = (
    ('de', gettext_noop('German')),
    ('en', gettext_noop('English')),
)

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True
USE_THOUSAND_SEPARATOR = False

LOCALE_PATHS = (
    PROJECT_DIR.child('locale'),
)

MEDIA_ROOT = PROJECT_DIR.child('template')
MEDIA_URL = '/media/'

STATIC_ROOT = PROJECT_DIR.child('static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJECT_DIR.child('assets'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = get_env_variable('GIRONIMOKEY')

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'gironimo.urls'

WSGI_APPLICATION = 'gironimo.wsgi.application'

TEMPLATE_DIRS = (
    PROJECT_DIR.child('templates'),
)

DEFAULT_FROM_EMAIL = 'mrochow@gironimo.org'
SEND_BROKEN_LINK_EMAILS = True
SERVER_EMAIL = 'mrochow@gironimo.org'

FIRST_DAY_OF_WEEK = 1

LANGUAGE_COOKIE_NAME = 'GIRONIMOLANG'
SESSION_COOKIE_NAME = 'GIRONIMOSESSION'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
