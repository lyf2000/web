from fastapi import FastAPI
from sqlalchemy import select

from db import SessionDep
from models import User
from crud import create_user as create_user_db
from schema import UserIn, UserOut


app = FastAPI()


@app.get("/")
async def index():
    return {}


@app.get("/users")
async def users(session: SessionDep) -> list[UserOut]:
    """user list"""
    users = select(User)
    users = session.execute(users).scalars().all()
    print(users)
    return [UserOut.model_validate(user) for user in users]


@app.post("/users")
async def create_user(session: SessionDep, user: UserIn) -> UserOut:
    """create user"""
    user = User(**user.model_dump())
    create_user_db(session, user)
    return UserOut.model_validate(user)
