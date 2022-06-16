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
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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


# Internationalization

LANGUAGES = (
    ('ru', gettext('Russian')),
    ('uk', gettext('Ukrainian')),
    ('en', gettext('English')),
)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_ROOT = env('HU_STATIC_ROOT')

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

MEDIA_ROOT = env('HU_MEDIA_ROOT')


# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LANGUAGES = (
#     ("ru", _("Russian")),
#     ("uk", _("Ukrainian")),
# )

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets"),
]

STOCKS_TYPES = (
    (0, 'Unconditional'),
    (1, 'Order items count'),
    (2, 'Conditional')
)

TRANSLATABLE_MODEL_MODULES = ["showcase.Categories", "showcase.Items", "showcase.Sizes",]