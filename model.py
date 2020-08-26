# -*- coding : <utf-8> -*-
# model.py

from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String

engine = create_engine('sqlite:///books.db', echo=True)
Base = declarative_base()


class Book(Base):
    """
    * The Book model : ブックテーブルを定義
    """
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

    def __init__(self, title, author):
        self.title = title
        self.author = author


class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    book_id = Column(ForeignKey("books.id"))
    book = relationship("Book", backref=backref("characters", order_by=id))

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def fullname(self):
        """
        * フルネームを返す
        """
        return "%s %s" % (self.first_name, self.last_name)

    def __repr__(self):
        """
        * 文字列の公式表現をオーバーライド
        """
        return "<Character(%s)>" % self.fullname


if __name__ == "__main__":
    # Create the table
    Base.metadata.create_all(engine)
    # Create a session object (データベースにデータを入力出来るようにする)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add data to the tables
    new_char = Character("直樹", "半沢")
    new_char.book = Book("オレたちバブル入行組", "池井戸潤")
    session.add(new_char)
    new_char = Character("アメリカ", "フェレーラ")
    new_char.book = Book("アグリー・ベティ", "シルヴィオ・ホルタ")
    session.add(new_char)
    session.commit()
