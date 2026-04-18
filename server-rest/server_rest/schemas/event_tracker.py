"""Schemas for event tracker API
"""

from pydantic import BaseModel, Field
from typing import Optional


class Event(BaseModel):
    """Schema for an event, payload for POST /event-tracker"""
    day: int = Field(..., ge=1, le=31, description="Day of the event (1-31)")
    month: int = Field(..., ge=1, le=12, description="Month of the event (1-12)")
    event_name: str = Field(..., min_length=1, max_length=255, description="Name of the event")


class EventFilter(BaseModel):
    """Schema for filtering events, query parameters for GET /event-tracker"""
    day: Optional[int] = Field(..., ge=1, le=31, description="Filter by day, (1-31)")
    month: Optional[int] = Field(..., ge=1, le=12, description="Filter by month, (1-12)")


class EventResponse(BaseModel):
    """Schema for event response, response model for GET /event-tracker"""
    event_id: str = Field(..., description="Unique identifier for the event")
    day: int = Field(..., ge=1, le=31, description="Day of the event (1-31)")
    month: int = Field(..., ge=1, le=12, description="Month of the event (1-12)")
    event_name: str = Field(..., min_length=1, max_length=255, description="Name of the event")
