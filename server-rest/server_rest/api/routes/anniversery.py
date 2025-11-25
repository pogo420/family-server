from fastapi import APIRouter
from server_rest.schemas.common import GenericMessage


router = APIRouter(
    prefix="/anniversary",
    tags=["anniversary"]
)


@router.get("/", response_model=GenericMessage)
def anniversary_root():
    return {"message": "Welcome to root endpoint of Anniversary manager api"}
