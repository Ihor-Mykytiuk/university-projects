from fastapi import APIRouter, HTTPException
from app.database import db
from app.repository import BookRepository
from app.models import Book
from typing import List

router = APIRouter(
    prefix="/books",
    tags=["books"],
    responses={404: {"description": "Not found"}},
)

repo = BookRepository(database=db)

@router.get("/", response_model=List[Book])
async def get_books():
    return await repo.find_by({})
