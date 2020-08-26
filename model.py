# -*- coding : <utf-8> -*-
# model.py

from sqlalchemy import Table, Column, create_engine
from sqlalchemy import Integer, ForeignKey, String, Unicode
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relation

engine = create_engine('sqlite:///books.db', echo=True)
Base = declarative_base()
metadata = Base.metadata


class OlvBook(object):
    """
    * Book model for ObjectListView
    """
    def __init__(self, id, title, author, isbn, publisher, last_name, first_name):
        self.id = id  # unique row id from database
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publisher = publisher
        self.last_name = last_name
        self.first_name = first_name


class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    first_name = Column("ファーストネーム", String(50))
    last_name = Column("ラストネーム", String(50))

    def __repr__(self):
        return "<Person: %s %s>" % (self.first_name, self.last_name)


class Book(Base):
    """
    * The Book model : ブックテーブルを定義
    """
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("people.id"))
    title = Column("title", Unicode)
    isbn = Column("isbn", Unicode)
    publisher = Column("publisher", Unicode)
    person = relation("Person", backref="books", cascade_backrefs=False)
