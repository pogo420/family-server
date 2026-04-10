"""Logic for logging setup
"""
import logging
from logging.handlers import RotatingFileHandler
import os

from server_rest.common import LOG_BACKUP_COUNT, LOG_DIR, LOG_NAME, MAX_LOG_SIZE


def setup_logging(enable_debug: bool):
    # Create logs directory if not exists
    os.makedirs(LOG_DIR, exist_ok=True)

    # Log format
    log_format = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    formatter = logging.Formatter(log_format)

    # Root logger
    logger = logging.getLogger()
    logging_level = logging.DEBUG if enable_debug else logging.INFO
    logger.setLevel(logging_level)

    # File Handler (rotation by size)
    file_handler = RotatingFileHandler(
        f"{LOG_DIR}/{LOG_NAME}",
        maxBytes=MAX_LOG_SIZE,        # Log size of each log
        backupCount=LOG_BACKUP_COUNT  # Keep last, given counts
    )
    file_handler.setFormatter(formatter)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Avoiding duplicate logs (important in reload/dev)
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
