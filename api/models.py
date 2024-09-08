from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from db import Base, SessionLocal


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)

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


# create_table_users()
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

# session = SessionLocal()
# with session.begin():
#     session.query(User).delete()  # delete all users
#     assert len(session.query(User).all()) == 0

#     user = User(id=1, email="efgdff")
#     session.add(user)
#     session.commit()

#     assert len(session.query(User).all()) == 1
#     session.rollback()
