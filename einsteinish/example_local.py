
#EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

'''
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

'''
# mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'einsteinishdb',
        'USER': 'root',                     # Not used with sqlite3.
        'PASSWORD': 'password',   # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


#SITE_ID = 1   # example.com       
#SITE_ID = 3   # einsteinish.com       
SITE_ID = 2   # localhost:8000

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'kihyuck.hong@gmail.com'
EMAIL_HOST_PASSWORD = 'email-password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

SECRET_KEY = 'einsteinishcom'
