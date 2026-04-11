"""Repository layer for db connection check.
Does RAW queries to db.
"""
from sqlalchemy import text
from sqlalchemy.orm import Session
import logging

# Local file logger
logger = logging.getLogger(__name__)


def get_db_version(db: Session) -> str | None:
    try:
        return db.execute(text("SELECT version();")).scalar()
    except Exception as e:
        logger.warning(f"Issue seen in getting db version:{str(e)}")
        return None
