"""
Django settings for house.

"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chores',
    'markdown_deux',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'house.urls'

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
                # 'django.core.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'house.wsgi.application'



# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/house/staticfiles/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles'),
)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


MEDIA_ROOT = os.path.join(BASE_DIR, 'house')

MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = '/accounts/loggedin/'

try:
    from house.localsettings import *
    print 'you''re using the local dev settings'
except ImportError:
    from house.prodsettings import *
