from fastapi import FastAPI
from server_rest.schemas.common import GenericMessage
app = FastAPI()


@app.get("/", response_model=GenericMessage)
def read_root():
    return {"message": "Welcome to root endpoint of family server rest"}
