from pathlib import Path
from dotenv import load_dotenv
import os
load_dotenv()
import logging.config
from django.utils.log import DEFAULT_LOGGING
from django.core.management.color import supports_color

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = int(os.environ.get("DEBUG", default=0))
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")



# --------------------------------------------------------------
# Installed apps
# --------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


THIRD_PARTY_APPS = [
    'django_extensions',
    'django_celery_beat',
    'widget_tweaks',
]

APPS = [
    'core',
    'tasks',
    'users',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + APPS

# --------------------------------------------------------------
# End Installed apps
# --------------------------------------------------------------

# --------------------------------------------------------------
# CELERY SETTINGS
# --------------------------------------------------------------
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://redis:6379")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BACKEND", "redis://redis:6379")
if CELERY_RESULT_BACKEND == 'django-db':
    INSTALLED_APPS += ['django_celery_results',]
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/London'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
# --------------------------------------------------------------
# END CELERY SETTINGS
# --------------------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'agi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'agi.wsgi.application'


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

LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'Europe/London'
USE_I18N = True
USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'

LOGIN_URL = "users:login"
LOGIN_REDIRECT_URL = "users:dashboard"
LOGOUT_REDIRECT_URL = "core:home"

LOGGING_CONFIG = None
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG' if DEBUG else 'INFO').upper()
LOG_FILE_PATH = os.environ.get('LOG_FILE_PATH')
CELERY_LOG_FILE_PATH = os.environ.get('CELERY_LOG_FILE_PATH')
CELERY_TASKS_LOGGER_NAME = "celery_tasks"

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            # see more parameters at https://docs.python.org/3/library/logging.html#logging.LogRecord
            'format': '[%(asctime)s,%(msecs)03d %(levelname)s %(filename)s:%(lineno)s|%(name)s] %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },

        'agi.json.formatter': {
            'class': 'utils.logger.agiJsonFormatter'
        },

        'colorlog': {
            'class': 'colorlog.ColoredFormatter',
            'format': '%(log_color)s[%(asctime)s,%(msecs)03d %(levelname)s %(filename)s:%(lineno)s|%(name)s] %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },

        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{asctime}] {message}',
            'datefmt': "%Y-%m-%d %H:%M:%S",
            'style': '{'
        }
    },
    'handlers': {
        'console': {
            'class': 'colorlog.StreamHandler' if supports_color() else 'logging.StreamHandler',
            'formatter': 'colorlog' if supports_color() else 'console',
            # 'filters': ['require_debug_true']
        },

        'rotating_file': {
            'class': 'utils.logger.BetterRotatingFileHandler',
            'formatter': 'agi.json.formatter',
            # 'filters': ['require_debug_true'],
            'filename': LOG_FILE_PATH,
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 10
        },
        'celery_rotating_file': {
            'class': 'utils.logger.BetterRotatingFileHandler',
            'formatter': 'agi.json.formatter',
            # 'filters': ['require_debug_true'],
            'filename': CELERY_LOG_FILE_PATH,
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 10
        },

        'django.server': DEFAULT_LOGGING['handlers']['django.server'],

    },
    'loggers': {
        # "root" logger which serves as a catch-all for any logs that are sent from any Python module
        '': {
            'level': 'ERROR',
            'handlers': ['console', 'rotating_file'],
        },

        'django': {
            'handlers': ['console', 'rotating_file'],
            'level': 'ERROR',
        },

        'django.request': {
            'handlers': ['console', 'rotating_file'],
            'level': LOG_LEVEL,
            'propagate': False,
        },

        # DB queries
        'django.db.backends': {
            'handlers': ['console', 'rotating_file'],
            'level': 'ERROR',
            'propagate': False,
        },

        # Logging From AGI App
        'agi': {
            'level': LOG_LEVEL,
            'handlers': ['console', 'rotating_file'],
            # required to avoid double logging with root logger
            'propagate': False,
        },

        'core': {
            'level': LOG_LEVEL,
            'handlers': ['console', 'rotating_file'],
            'propagate': False,
        },

        'users': {
            'level': LOG_LEVEL,
            'handlers': ['console', 'rotating_file'],
            'propagate': False,
        },

        CELERY_TASKS_LOGGER_NAME: {
            'level': LOG_LEVEL,
            'handlers': ['console', 'celery_rotating_file'],
            # required to avoid double logging with root logger
            'propagate': False,
        },

        # Django-internals logging
        'django.server': DEFAULT_LOGGING['loggers']['django.server'],

    },
})
