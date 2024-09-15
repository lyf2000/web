from sqlalchemy import select
from sqlalchemy.orm import Session

from models import User
from schema import UserIn


def create_user(session: Session, user: User) -> User:
    session.add(user)
    session.commit()
    # session.refresh(user)  # not necessary, just for tip
    return user


def get_user_by_id(session: Session, user_id: int) -> User | None:
    statement = select(User).filter(User.id == user_id).limit(1)
    return session.execute(statement).scalars().one_or_none()


def update_user(session: Session, user: User, user_in: UserIn) -> User:
    for key, val in user_in.model_dump().items():  # TODO refact
        setattr(user, key, val)
    session.commit()

    return user
