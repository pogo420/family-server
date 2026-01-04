from sqlalchemy.orm import Session
from server_rest.repository.db_test import get_db_version


def is_db_alive(db: Session) -> bool:
    version = get_db_version(db)
    if version:
        return True
    else:
        return False
