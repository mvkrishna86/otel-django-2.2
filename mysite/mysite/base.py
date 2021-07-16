import os
import base64
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = ["*"]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '{levelname} {asctime} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
    }
}

MY_APPS = [
    'nsl_vcs',
    'utility'
]

MY_LOGGERS = {}
MY_HANDLERS = {}
for app in MY_APPS:
    directory = BASE_DIR + "_logs/" + app + "/"
    if not os.path.exists(directory):
        os.makedirs(directory)

    MY_HANDLERS[app] = {
        'level': 'DEBUG',
        'class': 'logging.handlers.RotatingFileHandler',
        'filename': directory + '/' + str(datetime.date.today()) + '.log',
        'maxBytes': 1024*1024*5,
        'backupCount': 2,
        'formatter': 'simple'
    }

    MY_LOGGERS[app] = {
        'handlers': [app],
        'level': 'DEBUG',
        'propagate': True,
    }
LOGGING['handlers'].update(MY_HANDLERS)
LOGGING['loggers'].update(MY_LOGGERS)

# command to grant permission to the folder
#  sudo chown -R user /var/log/vcs

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

