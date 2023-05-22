from pydantic import BaseModel


class Appeal(BaseModel):
    name: str
    phone: str
