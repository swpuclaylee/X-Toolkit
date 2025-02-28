import os
import logging.config
from x_toolkit.config import Config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOG_DIR = os.path.join(BASE_DIR, Config.LOG_FOLDER)
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)


def get_logger(log_name):
    log_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "[%(asctime)s] [%(name)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "verbose"
            },
            "file": {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "when": "midnight",
                "interval": 1,
                "filename": f"{LOG_DIR}/{log_name}.log",
                "backupCount": 7,
                "level": "INFO",
                "formatter": "verbose",
                "encoding": "utf-8"
            }
        },
        "loggers": {
            log_name: {
                "handlers": ["console", "file"],
                "level": "INFO"
            }
        }
    }
    logging.config.dictConfig(log_config)
    return logging.getLogger(log_name)
