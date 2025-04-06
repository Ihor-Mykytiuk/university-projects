from fastapi import APIRouter, HTTPException
from app.database import db
from app.repository import BookRepository
from app.models import Book
from typing import List
from bson import ObjectId

router = APIRouter(
    prefix="/books",
    tags=["books"],
    responses={404: {"description": "Not found"}},
)

repo = BookRepository(database=db)


@router.get("/", response_model=List[Book])
async def get_books():
    return await repo.find_by({})


@router.get("/{book_id}", response_model=Book)
async def get_book(book_id: str):
    return await repo.find_one_by_id(ObjectId(book_id))


@router.post("/", status_code=201, response_model=Book)
async def add_book(book: Book):
    await repo.save(book)
    return book

@router.delete("/{book_id}", status_code=204)
async def delete_book(book_id: str):
    await repo.delete_by_id(ObjectId(book_id))
    return