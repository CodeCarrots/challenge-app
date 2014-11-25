"""
Django settings for challenge project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from django.contrib import messages

# Build paths inside the project like this: BASE_DIR / "directory"
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


# Use 12factor inspired environment variables
import environ
env = environ.Env()
# check if a file with local env/config exists in the base project dir
env_file = BASE_DIR / 'local.env'
if env_file.is_file():
    environ.Env.read_env(str(env_file))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'account',
    'crispy_forms',

    'challenge',
    'tasks',
    'accounts',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'account.middleware.LocaleMiddleware',
    'account.middleware.TimezoneMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'account.context_processors.account',
]


ROOT_URLCONF = 'challenge.urls'

WSGI_APPLICATION = 'challenge.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pl'

gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
    ('pl', gettext('Polish')),
)

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (str(BASE_DIR / 'locale'),)


MEDIA_ROOT = str(BASE_DIR / '_media')
STATIC_ROOT = str(BASE_DIR / '_static')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = [str(BASE_DIR / 'templates'), ]

STATICFILES_DIRS = [str(BASE_DIR / 'static'), ]

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Django Debug Toolbar
if DEBUG:
    INSTALLED_APPS += (
        'debug_toolbar.apps.DebugToolbarConfig',)

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_USE_OPENID = False
ACCOUNT_REQUIRED_EMAIL = False
ACCOUNT_EMAIL_UNIQUE = False
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = False
ACCOUNT_EMAIL_CONFIRMATION_EMAIL = False
ACCOUNT_LOGIN_REDIRECT_URL = 'tasks_home'
ACCOUNT_LOGOUT_REDIRECT_URL = 'home'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2

from django.contrib.messages import constants as message_constants
MESSAGE_LEVEL = message_constants.DEBUG

LOGIN_URL = 'account_login'

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}
