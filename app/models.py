from pydantic import BaseModel
from typing import Optional
from pydantic_mongo import PydanticObjectId

class Book(BaseModel):
    id: Optional[PydanticObjectId] = None
    title: str
    author: str
    published_year: int
