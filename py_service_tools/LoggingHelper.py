import logging
import sys


class LoggingHelper:
    _DEFAULT_LOGGING_FORMAT = "%(asctime)s [%(levelname)s] [%(threadName)s] [%(filename)s:%(lineno)d]: %(message)s"

    def __init__(self):
        pass

    @staticmethod
    def init_root_logger(level=logging.INFO):
        logger = logging.getLogger()
        logger.setLevel(level)
        return logger

    @staticmethod
    def add_stdout_logger(logger, level=logging.INFO):
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)
        handler.setFormatter(logging.Formatter(LoggingHelper._DEFAULT_LOGGING_FORMAT))
        logger.addHandler(handler)
        return logger
