from sqlalchemy import text
from sqlalchemy.orm import Session


def get_db_version(db: Session) -> str | None:
    try:
        return db.execute(text("SELECT version();")).scalar()
    except Exception:
        return None
