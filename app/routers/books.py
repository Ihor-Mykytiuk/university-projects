from fastapi import APIRouter, HTTPException, Query, Request

from app.database import SessionDep
from app.models import Book, BookCreate

router = APIRouter(
    prefix="/books",
    tags=["books"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_books(
        request: Request,
        session: SessionDep,
        limit: int = Query(1, ge=1),
        offset: int = Query(0, ge=0),
):
    books = session.query(Book).offset(offset).limit(limit).all()
    total_count = session.query(Book).count()

    prev_url = None
    next_url = None

    if offset > 0:
        prev_offset = max(0, offset - limit)
        prev_url = f"{request.url.scheme}://{request.url.netloc}{request.url.path}?limit={limit}&offset={prev_offset}"

    if offset + limit < total_count:
        next_offset = offset + limit
        next_url = f"{request.url.scheme}://{request.url.netloc}{request.url.path}?limit={limit}&offset={next_offset}"

    return {
        "books": books,
        "total_count": total_count,
        "prev_page": prev_url,
        "next_page": next_url
    }


@router.get("/{book_id}", response_model=Book)
async def get_book(book_id: int, session: SessionDep):
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.post("/", status_code=201, response_model=Book)
async def add_book(book: BookCreate, session: SessionDep):
    db_book = Book.model_validate(book)
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book


@router.delete("/{book_id}", status_code=204)
async def delete_book(book_id: int, session: SessionDep):
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    session.delete(book)
    session.commit()
    return
