from datetime import datetime

from pydantic import BaseModel


class Appeal(BaseModel):
    name: str
    phone: str
    completed: bool | None = None
    date_created: datetime | None = None
    date_update: datetime | None = None

    class Config:
        orm_mode = True
