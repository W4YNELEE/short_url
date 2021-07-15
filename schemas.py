from pydantic import BaseModel

class Item(BaseModel):
    url: str
    datetime: str
    short_url: str
    class Config:
        orm_mode = True

class ItemCreate(BaseModel):
    url: str