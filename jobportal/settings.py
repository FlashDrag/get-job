"""
Django settings for jobportal project.

Generated by 'django-admin startproject' using Django 3.2.19.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

development = os.getenv('DEVELOPMENT', False) == 'True'
if development:
    print('Development mode is ON.')
else:
    print('Development mode is OFF.')

DEBUG = os.getenv('DEBUG', False) == 'True'
if DEBUG:
    print('Debug mode is ON.')
else:
    print('Debug mode is OFF.')

SECRET_KEY = os.getenv('SECRET_KEY')


ALLOWED_HOSTS = ['127.0.0.1', 'localhost',
                 'get-job-dev.herokuapp.com',
                 'get-job.herokuapp.com',
                 'get-job.live',
                 'www.get-job.live']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django.contrib.staticfiles',
    'storages',
    'fontawesomefree',
    'crispy_forms',
    'crispy_bootstrap5',
    'sass_processor',
    'compressor',
    'core',
    'jobseeker',
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

ROOT_URLCONF = 'jobportal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATICFILES_FINDERS = [
    # Default finders
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # sass processor and compressor finders
    'sass_processor.finders.CssFinder',
]

WSGI_APPLICATION = 'jobportal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if development:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
    if os.getenv("DATABASE_URL", None) is None:
        raise Exception("DATABASE_URL environment variable not defined")

    # Parse database configuration from $DATABASE_URL
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config(
            default=os.getenv('DATABASE_URL')
        )
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# ___Static files (CSS, JavaScript, Images)___
# https://docs.djangoproject.com/en/3.2/howto/static-files/

if not development:
    # aws settings
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = None
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

    # s3 static settings
    AWS_LOCATION = 'static'
    # URL path for your static files where they will be served from
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
    STATICFILES_STORAGE = 'storage_backends.StaticStorage'

    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = 'media'
    # URL path for media files where they will be served from
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'storage_backends.PublicMediaStorage'
else:
    # URL path for your static files where they
    # will be served from during development
    STATIC_URL = '/static/'

    # URL path for media files where they will be served from
    MEDIA_URL = '/media/'
    # Dir where media files are stored during development
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Dir where your static files are stored during development
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), ]
# Dir where static files will be collected using
# python manage.py collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Dir where sass files are stored
SASS_PROCESSOR_ROOT = os.path.join(BASE_DIR, 'static')
# ___---___

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Set custom user model as default
AUTH_USER_MODEL = "core.User"


# ___Allauth___

# AUTHENTICATION_BACKENDS = [
#     # Needed to login by username in Django admin, regardless of `allauth`
#     'django.contrib.auth.backends.ModelBackend',

#     # `allauth` specific authentication methods, such as login by e-mail
#     'allauth.account.auth_backends.AuthenticationBackend',
#     ]

SITE_ID = 1

# Specifies the URL that the user will be redirected
# to after a successful login or logout.
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# No e-mail verification is required to complete the signup process.
ACCOUNT_EMAIL_VERIFICATION = 'none'
# Removes the username field from the signup form.
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# Requires the user to enter a unique e-mail address during signup.
ACCOUNT_EMAIL_REQUIRED = True
# Removes the username field from the signup form.
ACCOUNT_USERNAME_REQUIRED = False
# Remembers the user’s session after closing the browser.
ACCOUNT_SESSION_REMEMBER = True
# Allows the user to log in using their e-mail address and password.
ACCOUNT_AUTHENTICATION_METHOD = 'email'
# Prevents multiple signups with the same e-mail address.
ACCOUNT_UNIQUE_EMAIL = True
# Disables the e-mail verification when a user signs up.
ACCOUNT_EMAIL_VERIFICATION = 'none'


# ___Crispy bootstrap5___
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
