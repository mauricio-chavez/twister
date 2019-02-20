"""Django development settings for twister project."""

# Extends from base settings
from .base import *

DEBUG = True

ALLOWED_HOSTS += [
    '127.0.0.1',
    'localhost',
]

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

MEDIA_URL = "/media/"
MEDIA_ROOT = APPS_DIR / 'media'

CACHE_TIMEOUT = 30