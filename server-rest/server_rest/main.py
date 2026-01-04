from fastapi import FastAPI
from server_rest.schemas.common import GenericMessage
from server_rest.api.routes.db_test import router as db_test_router
from server_rest.core.config import get_settings


settings = get_settings()
app = FastAPI()


@app.get("/", response_model=GenericMessage)
def read_root():
    return {"message": f"Welcome to root endpoint of {settings.APP_NAME}"}


app.include_router(db_test_router)
