import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

DEBUG = True

ADMINS = (
     ('K Hong', 'contact.einsteinish@gmail.com'),
)

MANAGERS = ADMINS

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',
)

THIRD_PARTY_APPS = (
    'markdown_deux',
    'haystack',
    'django_extensions',
    'guardian',
    'widget_tweaks',
    'braces',
    'djangoratings',
    'disqus',
)

LOCAL_APPS = (
    'registration',
    'profiles',
    'resources',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'assets')

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'guardian.backends.ObjectPermissionBackend',
)

ALLOWED_HOSTS = []
TIME_ZONE = 'America/Tijuana'
LANGUAGE_CODE = 'en-us'

USE_I18N = False
USE_L10N = True
USE_TZ = False

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # insert your TEMPLATE_DIRS here
            os.path.join(PROJECT_ROOT, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:

                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.static',
                'django.template.context_processors.tz',
            ],
        },
    },
]


ROOT_URLCONF = 'einsteinish.urls'

WSGI_APPLICATION = 'einsteinish.wsgi.application'

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

#HAYSTACK settings
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.BaseSignalProcessor'
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 12
HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
            'URL': 'http://127.0.0.1:9200/',
            'INDEX_NAME': 'haystack',
        },
}
# For light traffic
# HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

#DJANGO extended settings we are using
LOGIN_REDIRECT_URL = '/resource/'
ABSOLUTE_URL_OVERRIDES = {
        'auth.user': lambda u: "/profile/%s/" % u.username,
}
SERVER_EMAIL = "kihyuck.hong@gmail.com"

#Django-Registration Settings
ACCOUNT_ACTIVATION_DAYS = 7
DEFAULT_FROM_EMAIL =  "kihyuck.hong@gmail.com"

#Django-Guardian Settings
ANONYMOUS_USER_ID = -1
GUARDIAN_RENDER_403 = True

#Django-Ratings Settings
RATINGS_VOTES_PER_IP = 2000 #TODO all votes are essentially from 127.0.0.1. This can lead to problems

#Disqus Settings
DISQUS_API_KEY = 'lTuOXBAfTK3symHWvi7cZHgcYipkL32BoSud7f0H4gl4lfVhVw0HCcbcmiu1rWJY'
DISQUS_WEBSITE_SHORTNAME = 'einsteinish'


'''
################################
# Moved to local_settings.py
# sqlite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'einsteinish.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'einsteinishuserdb',
        'USER': 'user',             # Not used with sqlite3.
        'PASSWORD': 'password',            # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Moved to local_settings.py
#SITE_ID = 1   # example.com       
#SITE_ID = 2   # einsteinish.com       
SITE_ID = 3   # localhost:8000

# Moved to local_settings.py
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'kihyuck.hong@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Moved to local_settings.py
SECRET_KEY = 'einsteinishcom'
################################
'''


#Import Local and Prod settings
try:
    from local_settings import *
except ImportError:
    pass

try:
    from prod_settings import *
except ImportError:
    pass
