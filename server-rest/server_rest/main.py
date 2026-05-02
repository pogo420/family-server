"""Main application file for the FastAPI application"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from server_rest.core.logging import setup_logging
from server_rest.schemas.common import GenericMessage
from server_rest.api.routes.event_tracker import router as event_tracker_router
from server_rest.api.routes.db_test import router as db_test_router
from server_rest.core.config import get_settings

# Allow only angular app to bypass CORS
origins = [
    "http://localhost:4200",  # Angular
]

# Getting settings
settings = get_settings()
# Setting up logger
setup_logging(settings.ENABLE_DEBUG)
# Local file logger
logger = logging.getLogger(__name__)
app = FastAPI(root_path="/api")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # allowed frontend URLs
    allow_credentials=True,
    allow_methods=["*"],          # GET, POST, DELETE, etc.
    allow_headers=["*"],          # all headers
)


@app.get("/", response_model=GenericMessage)
def read_root():
    logger.info("Handling root endpoint")
    return {"message": f"Welcome to root endpoint of {settings.APP_NAME}"}


# Include routers for different API endpoints
app.include_router(db_test_router)
app.include_router(event_tracker_router)
