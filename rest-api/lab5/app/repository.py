from pydantic_mongo import AsyncAbstractRepository
from app.models import Book

class BookRepository(AsyncAbstractRepository[Book]):
    class Meta:
        collection_name = "books"
