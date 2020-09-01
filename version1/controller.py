# -*- coding : <utf-8> -*-
# controller.py

from model import Book, Person, OlvBook
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def add_record(session, data):
    book = Book()
    book.title = data["book"]["title"]
    book.isbn = data["book"]["isbn"]
    book.publisher = data["book"]["publisher"]
    author = Person()
    author.first_name = data["author"]["first_name"]
    author.last_name = data["author"]["last_name"]
    book.person = author

    # try:
    session.add(book)
    session.commit()
    # except Exception as e:
    #     print("add Error : %s" % e )
    #     session.rollback()


def connect_to_database():
    engine = create_engine("sqlite:///books.db", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def convert_results(results):
    books = []
    for record in results:
        author = "%s %s" % (record.person.first_name, record.person.last_name)
        book = OlvBook(record.id, record.title, author, record.isbn,
                       record.publisher, record.person.last_name, record.person.first_name)
        books.append(book)
    return books


def delete_record(session, id_num):
    record = session.query(Book).filter_by(id=id_num).one()
    session.delete(record)
    session.commit()


def edit_record(session, id_num, row):
    record = session.query(Book).filter_by(id=id_num).one()
    record.title = row["title"]
    record.person.first_name = row["first_name"]
    record.person.last_name = row["last_name"]
    record.isbn = row["isbn"]
    record.publisher = row["publisher"]
    session.add(record)
    session.commit()


def get_all_records(session):
    result = session.query(Book).all()
    books = convert_results(result)
    return books


def search_records(session, filter_choice, keyword):
    if filter_choice == "Author":
        qry = session.query(Person)
        result = qry.filter(Person.first_name.contains('%s' % keyword)).all()
        records = []
        for record in result:
            for book in record.books:
                records.append(book)
        result = records
    elif filter_choice == "Title":
        qry = session.query(Book)
        result = qry.filter(Book.title.contains('%s' % keyword)).all()
    elif filter_choice == "ISBN":
        qry = session.query(Book)
        result = qry.filter(Book.isbn.contains('%s' % keyword)).all()
    else:
        qry = session.query(Book)
        result = qry.filter(Book.publisher.contains('%s' % keyword)).all()
    books = convert_results(result)

    return books


def setup_database():
    super().metadata.create_all()
