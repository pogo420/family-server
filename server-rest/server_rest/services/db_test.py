"""Service logic for db connection check.
Does API calls to repository layer
"""
from sqlalchemy.orm import Session
import logging

from server_rest.repository.db_test import get_db_version

# Local file logger
logger = logging.getLogger(__name__)


def is_db_alive(db: Session) -> bool:
    version = get_db_version(db)
    logger.debug(f"Received DB version: {version}")
    if version:
        return True
    else:
        return False
