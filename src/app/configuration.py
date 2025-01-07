import configparser
import os

from .logger_api import LoggerApi

__version__ = '0.0.1'

LOGGER = LoggerApi("api-messages")

conf_file = os.getenv('CONF_FILE', './conf/config.cfg')

config = configparser.ConfigParser()
config.read(conf_file)

API_IP = config.get('conf', "api_ip", fallback='0.0.0.0')
API_PORT = int(os.getenv('PORT', 10000))
API_KEY = os.getenv('API_KEY', 'token')
SAVE_FOLDER = config.get('conf', 'SAVE_FOLDER', fallback='./save')
MINUTES_REFRESH_CONF = config.getint('conf', "minutes_refresh_conf",
                                     fallback=5)
cors_ = config.get('conf', "cors_origins", fallback='').split(',')
CORS_ORIGINS = [c_ for c_ in cors_ if c_ != '']

LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "app.utils.logger_api.ColoredFormatter",
            "format": LOGGER.msg_format,
            "datefmt": LOGGER.datetime_format,
        },
        "filefrmt": {
            "format": LOGGER.msg_format,
            "datefmt": LOGGER.datetime_format,
        },

    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "DEBUG",
        },
        "file": {
            "()": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "filefrmt",
            "level": "DEBUG",
            "filename": LOGGER.file_name,
            "when": "midnight",
            "interval": 1,
            "backupCount": 4,
        },
    },
    "loggers": {
        "": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
        },
        "uvicorn.error": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": False,
        },
        "uvicorn.access": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}

MAIL_FROM = os.getenv("MAIL_FROM", None)
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", None)


