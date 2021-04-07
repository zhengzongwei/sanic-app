import logging
import os

from .constant import *

log = logging.getLogger(__name__)

log_path = BASE_DIR + "/logs"
if not os.path.exists(log_path):
    os.mkdir(log_path)

LOG_SETTINGS = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'default'
        },
        'error': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'debug',
            'filename': log_path + '/error.log',
            'maxBytes': LOG_MAX_BYTES,
            'backupCount': 5,
            'encoding': 'utf-8'
        },
    },
    'formatters': {
        'default': {
            # %(asctime)s - (%(name)s)[%(levelname)s][%(host)s]: %(request)s %(message)s %(status)d %(byte)d
            'format': '%(asctime)s - (%(name)s)[%(levelname)s][%(host)s]: %(request)s %(message)s %(status)d %(byte)d',
        },
        'debug': {
            'format': '%(asctime)s - %(levelname)s - %(name)s:%(lineno)d | %(message)s',
        }
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['console', 'error'],
            'propagate': True
        },
    }

}
