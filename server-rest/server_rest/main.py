"""Main application file for the FastAPI application"""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server_rest.api.routes.asset_tracker import router as asset_tracker_router
from server_rest.api.routes.db_test import router as db_test_router
from server_rest.api.routes.event_tracker import router as event_tracker_router
from server_rest.core.config import get_settings
from server_rest.core.logging import setup_logging
from server_rest.mqtt.subscriber import MQTTSubscriber
from server_rest.schemas.common import GenericMessage

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


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Setting up MQTT subscriber
    mqtt_subscriber = MQTTSubscriber(
        host=settings.MQTT_HOST,
        port=settings.MQTT_PORT,
        client_id=settings.MQTT_CLIENT_ID,
        username=settings.MQTT_USERNAME,
        password=settings.MQTT_PASSWORD,
    )

    try:
        logger.info("Starting MQTT subscriber")
        mqtt_subscriber.start()
        app.state.mqtt_subscriber = mqtt_subscriber
        yield

    finally:
        logger.info("Stopping MQTT subscriber")
        mqtt_subscriber.stop()


app = FastAPI(root_path="/api", lifespan=lifespan)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # allowed frontend URLs
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, DELETE, etc.
    allow_headers=["*"],  # all headers
)


@app.get("/", response_model=GenericMessage)
def read_root():
    logger.info("Handling root endpoint")
    return {"message": f"Welcome to root endpoint of {settings.APP_NAME}"}


# Include routers for different API endpoints
app.include_router(db_test_router)
app.include_router(event_tracker_router)
app.include_router(asset_tracker_router)
