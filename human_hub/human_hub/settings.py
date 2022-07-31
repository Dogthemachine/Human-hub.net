from pathlib import Path
import environ
import os

gettext = lambda s: s
from django.utils.translation import gettext_lazy as _


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ '*'
    # 'human-hub.net',
    # 'www.human-hub.net',
]

USE_I18N = True

# Application definition

INSTALLED_APPS = [
    'cacheops',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'administration.apps.AdministrationConfig',
    'orders.apps.OrdersConfig',
    'showcase.apps.ShowcaseConfig',
    'info.apps.InfoConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'showcase.middleware.force_default_language_middleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.session_middleware',
    'orders.middleware.info_middleware',
]

ROOT_URLCONF = 'human_hub.urls'

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
                'django.template.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'human_hub.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation

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

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ.get('REDIS_PORT') + "/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}

CACHEOPS_REDIS = os.environ.get('REDIS_PORT') + "/1"

CACHEOPS_DEFAULTS = {
    'timeout': 60*60
}

CACHEOPS = {
    'showcase.*': {'ops': 'all'},
}


# Internationalization

LANGUAGES = (
    ('uk', gettext('Ukrainian')),
    ('ru', gettext('Russian')),
    ('en', gettext('English')),
)

LANGUAGE_CODE = 'uk'

USE_TZ = True

USE_I18N = True

STATIC_ROOT = env('HU_STATIC_ROOT')

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

MEDIA_ROOT = env('HU_MEDIA_ROOT')

TIME_ZONE = 'Europe/Kiev'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOCALE_PATHS = (
  os.environ.get('TC_LOCALE_PATH'),
)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets"),
]

STOCKS_TYPES = (
    (0, 'Unconditional'),
    (1, 'Order items count'),
    (2, 'Conditional')
)

TRANSLATABLE_MODEL_MODULES = ["showcase.Categories", "showcase.Items", "showcase.Sizes",]

PRIVAT_CARD = os.environ.get('TC_PRIVAT_CARD')
MONO_CARD = os.environ.get('TC_MONO_CARD')
PRIVAT_NAME = os.environ.get('TC_PRIVAT_NAME')
MONO_NAME = os.environ.get('TC_MONO_NAME')

