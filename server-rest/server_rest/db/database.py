"""Logic for DB connection handling
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from server_rest.core.config import get_settings

settings = get_settings()
engine = create_engine(
    settings.DB_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
