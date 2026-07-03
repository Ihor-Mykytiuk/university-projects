from pydantic import BaseModel, Field
from typing import Optional
from pydantic_mongo import PydanticObjectId
from datetime import datetime


class BookBase(BaseModel):
    title: str = Field(..., max_length=100)
    author: str = Field(..., max_length=255)
    published_year: int = Field(..., ge=1000, le=datetime.now().year)


class Book(BookBase):
    id: Optional[PydanticObjectId] = None


class BookCreate(BookBase):
    pass
