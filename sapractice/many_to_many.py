from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, query, aliased, synonym

from sapractice.config import base, create_session, metadata


author_books = Table('author_books', metadata,
     Column('book_id', ForeignKey('books.id'), primary_key=True),
     Column('author_id', ForeignKey('authors.id'), primary_key=True)
)


class Book(base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)

    authors = relationship('Author', secondary=author_books, back_populates='books', lazy='dynamic')

    name = synonym('title')

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return self.title


class Author(base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    books = relationship('Book', secondary=author_books, back_populates='authors')

    def __repr__(self):
        return self.name + '-' + str(self.age)


if __name__ == '__main__':

    session = create_session()
    metadata.create_all()
    books = list()

    book = Book(title='book')
    authors = list()
    for i in range(10):
        book.authors.append(Author(name=f'author{i}', age=25+i))

    for a in book.authors:
        print(a)

    for i in range(5):
        book.authors[0].books.append(Book(title=f'book{i}'))

    for b in book.authors[0].books:
        print(b)

    for b in book.authors[0].books:
        print(b.name)

    session.commit()
