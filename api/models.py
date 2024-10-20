from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from db import Base, SessionLocal
# def get_sqlite_version():
#     session = SessionLocal()
#     from sqlalchemy import text

#     sql = text("SELECT sqlite_version();")
#     result = session.execute(sql).fetchone()
#     session.close()
#     return result[0]


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)

    # items = relationship("Item", back_populates="owner")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey("users.id"))

# owner = relationship("User", back_populates="items")


def create_table_users():
    session = SessionLocal()
    from sqlalchemy import text

    sql = text(
        """CREATE TABLE users (
        id INTEGER,
        email TEXT,
        PRIMARY KEY(id)
    )"""
    )
    # CHECK(email LIKE '%_@__%.__%'),
    session.execute(sql)
    session.close()

def create_table_books():
    session = SessionLocal()
    from sqlalchemy import text

    sql = text(
        """CREATE TABLE books (
        id INTEGER,
        title TEXT,
        author_id INTEGER,
        FOREIGN KEY(author_id) REFERENCES users(id) ON DELETE CASCADE,
        PRIMARY KEY(id)
    )"""
    )
    session.execute(sql)
    session.close()

# create_table_users()
# create_table_books()
# session = SessionLocal()
# print(session.query(User).all())  # []


# create_table_users()


def create_user():
    session = SessionLocal()
    user = User(email="efgdff")

    session.add(user)
    session.commit()

def create_book():
    session = SessionLocal()
    book = Book(title="efgdff", author_id=1)

    session.add(book)
    session.commit()

# create_user()  # no error, but not created
# create_book()


def remove_user(user_id: int):
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
    session.close()

remove_user(1)

# session = SessionLocal()
# print(session.query(User).all())  # []


def create_user():
    session = SessionLocal()
    user = User(id=1, email="efgdff")

    session.add(user)
    session.commit()  # new line


# create_user()

# session = SessionLocal()
# print(session.query(User).all())  # [User]

# session = SessionLocal()
# with session.begin():
#     session.query(User).delete()  # delete all users
#     assert len(session.query(User).all()) == 0

#     user = User(id=1, email="efgdff")
#     session.add(user)
#     session.commit()

#     assert len(session.query(User).all()) == 1
#     session.rollback()




# Поясняшка за primary key
# class Group(Base):
#     id

# class Subscribtion(Base):
#     __tablename__ = 'subscriptions'
#     user_id = Column(Integer, ForeignKey("users.id"))
#     group_id = Column(Integer, ForeignKey("groups.id"))
#     date_joined = Column(DateTime)

#     __table_args__ = (
#         sqlalchemy.PrimaryKeyConstraint('user_id', 'group_id'),
#     )

#     [
#         Subscribtion(user_id=1, group_id=1), # PrimaryKeyConstraint (1, 1)
#         Subscribtion(user_id=1, group_id=2), # PrimaryKeyConstraint (1, 2)
#         Subscribtion(user_id=2, group_id=1), # PrimaryKeyConstraint (2, 1)
#         Subscribtion(user_id=2, group_id=1), # PrimaryKeyConstraint (2, 1)  # ошибка
#     ]
# insert into subscriptions (user_id, group_id) values (1, 1)
# insert into subscriptions (user_id, group_id) values (1, 2)
# insert into subscriptions (user_id, group_id) values (2, 1)
# insert into subscriptions (user_id, group_id) values (2, 1)  # ошибка

# class User:
#     id
