"""Logic for logging setup"""

import logging


def setup_logging(enable_debug: bool):
    # Create logs directory if not exists
    # os.makedirs(LOG_DIR, exist_ok=True)

    # Log format
    log_format = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    formatter = logging.Formatter(log_format)

    # Root logger
    logger = logging.getLogger()
    logging_level = logging.DEBUG if enable_debug else logging.INFO
    logger.setLevel(logging_level)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Avoiding duplicate logs (important in reload/dev)
    if not logger.handlers:
        # logger.addHandler(file_handler)
        logger.addHandler(console_handler)
