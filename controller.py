# -*- coding : <utf-8> -*-
# controller.py

from model import Book, Person, OlvBook
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def add_recourd(session, data):
    """
    * Data should be a dictionary of two dictionaries in the following format:
    *    {"author":{"first_name":"John", "last_name":"Doe"},
    *   "book":{"title":"Some book", "isbn":"1234567890",
    *    "publisher":"Packt"}}
    """
    book = Book()
    book.title = data["book"]["title"]
    book.isbn = data["book"]["isbn"]
    book.publisher = data["book"]["publisher"]
    author = Person()
    author.first_name = data["author"]["first_name"]
    author.last_name = data["author"]["last_name"]
    book.publisher = author

    session.add(book)
    session.commit()
