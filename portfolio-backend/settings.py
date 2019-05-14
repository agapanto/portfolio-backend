"""
Django settings for portfolio-backend project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = eval(
    os.environ.get('DEBUG', 'False')
)

ALLOWED_HOSTS = [
    os.environ.get(
        'APP_HOST'
    ),
    os.environ.get(
        'WEBSITE_HOST',
        '127.0.0.1'
    ),
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    # Security & multi-app management
    'rest_framework_apicontrol',
    'rest_framework_jwt',
    'rest_framework_auth0',
    # Project specific apps
    'agapanto_portfolios',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio-backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'portfolio-backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Definitive configuration
DO_SPACES_ACCESS_KEY_ID = os.environ.get(
    'DO_SPACES_ACCESS_KEY_ID'
)
DO_SPACES_SECRET_ACCESS_KEY = os.environ.get(
    'DO_SPACES_SECRET_ACCESS_KEY'
)
DO_SPACES_SPACE_NAME = os.environ.get(
    'DO_SPACES_SPACE_NAME'
)
DO_SPACES_SPACE_FOLDER = os.environ.get(
    'DO_SPACES_SPACE_FOLDER'
)
DO_SPACES_ENDPOINT_URL = os.environ.get(
    'DO_SPACES_ENDPOINT_URL'
)
DO_SPACES_CACHE_MAX_AGE = int(
    os.environ.get(
        'DO_SPACES_CACHE_MAX_AGE'
    )
)
DO_SPACES_DEFAULT_ACL = None

# Get DEFAULT_ACL from env vars
try:
    DEFAULT_ACL = os.environ.get(
        'DO_SPACES_DEFAULT_ACL'
    )

    if DEFAULT_ACL != 'None':
        DO_SPACES_DEFAULT_ACL = DEFAULT_ACL

except Exception as e:
    pass

# Set File locations
DO_SPACES_STATIC_LOCATION = '{FOLDER}/static'.format(
    FOLDER=DO_SPACES_SPACE_FOLDER
)
DO_SPACES_PUBLIC_MEDIA_LOCATION = '{FOLDER}/media/public'.format(
    FOLDER=DO_SPACES_SPACE_FOLDER
)
DO_SPACES_PRIVATE_MEDIA_LOCATION = '{FOLDER}/media/private'.format(
    FOLDER=DO_SPACES_SPACE_FOLDER
)

#  Static files config
STATIC_URL = 'https://{ENDPOINT_URL}/{STATIC_LOCATION}/'.format(
    ENDPOINT_URL=DO_SPACES_ENDPOINT_URL,
    STATIC_LOCATION=DO_SPACES_STATIC_LOCATION
)

# Configure file storage settings
STATICFILES_STORAGE = 'storages.backends.do_spaces.DigitalOceanSpacesStaticStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.do_spaces.DigitalOceanSpacesPublicMediaStorage'
PRIVATE_FILE_STORAGE = 'storages.backends.do_spaces.DigitalOceanSpacesPrivateMediaStorage'


# REST FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # AUTH0 for users request(through Client apps)
        'rest_framework_auth0.authentication.Auth0JSONWebTokenAuthentication',
        # Rest Framework tokens for API Request(e.g.: Website integration )
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        # 'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
}

# AUTH0
AUTH0 = {
  'CLIENTS': {
      'default': {
          'AUTH0_CLIENT_ID': os.environ.get('AUTH0_CLIENT_ID'),
          'AUTH0_CLIENT_SECRET': os.environ.get('AUTH0_CLIENT_SECRET'),
          'CLIENT_SECRET_BASE64_ENCODED': eval(os.environ.get('AUTH0_CLIENT_SECRET_BASE64_ENCODED', 'False')),
          'AUTH0_ALGORITHM': 'HS256',
      }
  },
  'JWT_AUTH_HEADER_PREFIX': 'JWT',
  'AUTHORIZATION_EXTENSION': False,
  'REPLACE_PIPE_FOR_DOTS_IN_USERNAME': True,
  'USERNAME_FIELD': 'sub',
}

CORS_ORIGIN_ALLOW_ALL = eval(
    os.environ.get(
        'CORS_ORIGIN_ALLOW_ALL',
        'False',
    )
)

CORS_ORIGIN_WHITELIST = (
    '{WEBSITE_HOST}:{WEBSITE_PORT}'.format(
        WEBSITE_HOST=os.environ.get(
            'WEBSITE_HOST',
            '127.0.0.1'
        ),
        WEBSITE_PORT=os.environ.get(
            'WEBSITE_PORT',
            ''
        ),
    ).rstrip(':')
)
