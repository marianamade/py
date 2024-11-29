from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Django By Example",
        "author": "Antonio Mele",
        "publisher": "Packt Publishing Ltd",
        "published_date": "2022-01-19",
        "page_count": 1023,
        "language": "English",
    },
    {
        "id": 3,
        "title": "The web socket handbook",
        "author": "Alex Diaconu",
        "publisher": "Xinyu Wang",
        "published_date": "2021-01-01",
        "page_count": 3677,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Head first Javascript",
        "author": "Hellen Smith",
        "publisher": "Oreilly Media",
        "published_date": "2021-01-01",
        "page_count": 540,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Algorithms and Data Structures In Python",
        "author": "Kent Lee",
        "publisher": "Springer, Inc",
        "published_date": "2021-01-01",
        "page_count": 9282,
        "language": "English",
    },
    {
        "id": 6,
        "title": "Head First HTML5 Programming",
        "author": "Eric T Freeman",
        "publisher": "O'Reilly Media",
        "published_date": "2011-21-01",
        "page_count": 3006,
        "language": "English",
    },
]

class book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


class BookUpdateModel(BaseModel) :
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

@app.get("/books", response_model=List[book], tags=["books"])
async def get_all_books():
    return books 

@app.post("/books", tags=["books"], status_code= status.HTTP_201_CREATED)
async def create_book(book_data: book) -> dict :
    new_book = book_data.model_dump()

    books.append(new_book)
    return new_book

@app.get("/book/{book_id}", tags=["books"])
async def get_book(book_id: int) -> dict :
    for book in books:
        if book["id"] == book_id:
            return book 
        
        raise HTTPException(status_code=404, detail="book not found")

@app.patch("/book/{book_id}", tags=["books"])
async def update_book(book_id: int, book_update_data: BookUpdateModel) -> dict :
    for book in books:
        if book["id"] == book_id:
            book.update(book_update_data)
            return book
        
        raise HTTPException(status_code=404, detail="book not found")

@app.delete("/book/{book_id}", tags=["books"])
async def delete_book(book_id: int):
     for book in books:
         if book["id"] == book_id:
             books.remove(book)
             return {"message": "books deleted successfully"}
         
         raise HTTPException(status_code=404, detail="book not found")
