"""
Django settings for find_artek project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os

#### LPAP ####
# import ldap
# from django_auth_ldap.config import LDAPSearch, GroupOfNamesType
# ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
#### LPAP ####


# Load .env file
# Import load_dotenv
from dotenv import load_dotenv
# load .env file from 
dotenv_path = '/usr/src/project/.devcontainer/.env'
load_dotenv(dotenv_path=dotenv_path)




# from django_auth_ldap.config import LDAPSearch, GroupOfNamesType
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# get secret key from .env file
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# if 
DEBUG = False


# CAS_SERVER_URL = 'https://auth.dtu.dk/dtu/' # no multifactor
CAS_SERVER_URL = 'https://auth2.dtu.dk/dtu/' # with multifactor
CAS_VERSION = '2'
# Application definition


ALLOWED_HOSTS = [
    'find-artek.vezit.net',
    'find.artek.byg.dtu.dk',
    'find-artek-httpd-service',
    'localhost',
    
]

# Media url
MEDIA_ROOT = os.path.join('/mnt/shared-project-data/find_artek_static/media')
MEDIA_URL = '/media/'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django.contrib.gis',
    'publications',
    'django_cas_ng',
    'rest_framework',
    'drf_yasg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'find_artek.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'find_artek.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.spatialite',
#         'NAME': BASE_DIR / 'find_artek_new.sqlite',
#     },
#     'OPTIONS': {
#         'spatialite': {
#             'library_path': '/usr/lib/x86_64-linux-gnu/mod_spatialite.so',
#         }
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'find-artek-1',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'find-artek-db',
        'PORT': '5432',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'find-artek-1',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         'HOST': 'find-artek-db',
#         'PORT': '5432',
#     }
# }
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

# the docker volume dedicated to apache server is also secretly mounted here to conviently overwrite create the static files
# python manage.py collectstatic
# sets up the static files for the webserver
# BASE_DIR = '/usr/src/find_artek/app'
STATIC_ROOT = os.path.join('/mnt/shared-project-data/find_artek_static/staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_cas_ng.backends.CASBackend',
)


#### LPAP ####
# AUTHENTICATION_BACKENDS = (
#     'django_auth_ldap.backend.LDAPBackend',
#     'django.contrib.auth.backends.ModelBackend',
# )

# AUTH_LDAP_SERVER_URI = "ldaps://win.dtu.dk"

# AUTH_LDAP_BIND_DN = "CN=sus-pit-artek-ad-read,OU=Funktionskonti,OU=BYG,OU=Institutter,DC=win,DC=dtu,DC=dk"

# # Read the LDAP bind password from the file
# with open('secret/AUTH_LDAP_BIND_PASSWORD.txt', 'r') as f:
#     AUTH_LDAP_BIND_PASSWORD = f.read().strip()

# AUTH_LDAP_USER_SEARCH = LDAPSearch("OU=DTUBaseUsers,DC=win,DC=dtu,DC=dk",
#                                    ldap.SCOPE_SUBTREE,
#                                    "(sAMAccountName=%(user)s)")

# AUTH_LDAP_GROUP_SEARCH = LDAPSearch("DC=win,DC=dtu,DC=dk",
#                                     ldap.SCOPE_SUBTREE,
#                                     "(objectClass=group)")

# AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()

# AUTH_LDAP_USER_ATTR_MAP = {
#     "first_name": "givenName",
#     "last_name": "sn",
#     "email": "mail"
# }
#### LPAP ####


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
