from .settings import *
import os
import dj_database_url

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']

BLACKLIST_APPS = ['debugtoolbar', 'django_extensions']

INSTALLED_APPS = tuple([app for app in INSTALLED_APPS if app not in BLACKLIST_APPS])

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROXY', 'https')

ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'