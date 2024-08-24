from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db import Base, SessionLocal, get_db


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)

    # items = relationship("Item", back_populates="owner")


# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True)
#     title = Column(String, index=True)
# owner_id = Column(Integer, ForeignKey("users.id"))

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
    session.execute(sql)
    session.close()


# session = SessionLocal()
# print(session.query(User).all())  # []


# create_table_users()


def create_user():
    session = SessionLocal()
    user = User(id=1, email="efgdff")

    session.add(user)


# create_user()  # no error, but not created


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
