"""File containing schemas(pydantic) which are common in all routes, service
e.t.c

"""

from pydantic import BaseModel


class GenericMessage(BaseModel):
    message: str
