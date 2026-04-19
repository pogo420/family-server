"""Event tracker model, Table definition for event tracker API"""
from sqlalchemy import Column, Integer, String, UniqueConstraint
from server_rest.db.database import Base


class EventTracker(Base):
    __tablename__ = "event_tracker"

    event_id = Column(String(36), primary_key=True, index=True)
    day = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    event_name = Column(String(255), nullable=False)

    __table_args__ = (
        UniqueConstraint('day', 'month', 'event_name', name='uq_event_tracker_day_month_name'),
    )
