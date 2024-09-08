from sqlalchemy.orm import Session

from models import User


def create_user(session: Session, user: User) -> User:
    session.add(user)
    session.commit()
    # session.refresh(user)  # not necessary, just for tip
    return user
