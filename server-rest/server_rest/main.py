from fastapi import FastAPI
import logging

from server_rest.core.logging import setup_logging
from server_rest.schemas.common import GenericMessage
from server_rest.api.routes.db_test import router as db_test_router
from server_rest.core.config import get_settings

# Getting settings
settings = get_settings()
# Setting up logger
setup_logging(settings.ENABLE_DEBUG)
# Local file logger
logger = logging.getLogger(__name__)
app = FastAPI(root_path="/api")


@app.get("/", response_model=GenericMessage)
def read_root():
    logger.info("Handling root endpoint")
    return {"message": f"Welcome to root endpoint of {settings.APP_NAME}"}


app.include_router(db_test_router)
