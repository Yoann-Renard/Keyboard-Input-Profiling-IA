import logging

from modules.Settings import LOGGING_FORMAT, LOGGING_FILEMODE, LOGGING_LEVEL, LOGGING_FILE

logger = logging.getLogger("logger")

logger_handler = logging.FileHandler(filename=LOGGING_FILE, mode=LOGGING_FILEMODE)
logger_handler.setFormatter(logging.Formatter(LOGGING_FORMAT))
logger.setLevel(level=LOGGING_LEVEL)
logger.addHandler(logger_handler)