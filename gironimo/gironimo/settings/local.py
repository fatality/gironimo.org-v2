from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": get_env_variable('GIRONIMODB'),
        "USER": get_env_variable('DBUSER'),
        "PASSWORD": get_env_variable('DBPASS'),
        "HOST": "localhost",
        "PORT": "",
    }
}

INSTALLED_APPS += ("debug_toolbar",)
INTERNAL_IPS = ("127.0.0.1",)
MIDDLEWARE_CLASSES += ("debug_toolbar.middleware.DebugToolbarMiddleware",)

SEND_BROKEN_LINK_EMAILS = False
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
