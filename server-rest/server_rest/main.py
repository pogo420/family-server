from fastapi import FastAPI
from server_rest.schemas.common import GenericMessage
from server_rest.api.routes.anniversery import router as anniversery_router


app = FastAPI()


@app.get("/", response_model=GenericMessage)
def read_root():
    return {"message": "Welcome to root endpoint of family server rest"}


app.include_router(anniversery_router)
