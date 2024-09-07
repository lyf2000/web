from sqlalchemy import Integer, String, Column  # , Boolean, ForeignKey
# from sqlalchemy.orm import relationship

from db import Base, SessionLocal


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
    from sqlalchemy import text
    session = SessionLocal()

    sql = text(
        """CREATE TABLE IF NOT EXISTS users(
        id INTEGER,
        email TEXT,
        PRIMARY KEY(id)
        )"""
    )
    session.execute(sql)
    session.close()


def create_user(email: str):
    session = SessionLocal()
    user = User(email=email)

    session.add(user)
    session.commit()


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
