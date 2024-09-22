from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from db import SessionDep
from models import User
from crud import (
    delete_user as delete_user_db,
    create_user as create_user_db,
    get_user_by_id,
    get_users,
    update_user as update_user_db,
)
from schema import UserIn, UserOut


app = FastAPI()


@app.get("/")
async def index():
    return {}


@app.get("/users")
async def users(session: SessionDep) -> list[UserOut]:
    """user list"""
    users = get_users(session)
    print(users)
    return [UserOut.model_validate(user) for user in users]


@app.get("/users/{user_id}")
async def get_user(session: SessionDep, user_id: int) -> UserOut:
    """get user"""
    user = get_user_by_id(session, user_id)
    if not user:
        raise HTTPException(detail="User not found", status_code=404)

    return UserOut.model_validate(user)


@app.post("/users")
async def create_user(session: SessionDep, user: UserIn) -> UserOut:
    """create user"""
    user = User(**user.model_dump())
    create_user_db(session, user)
    return UserOut.model_validate(user)


@app.put("/users/{user_id}")
async def update_user(session: SessionDep, user_id: int, user_in: UserIn) -> UserOut:
    """update user"""
    user = get_user_by_id(session, user_id)
    if not user:
        raise HTTPException(detail="User not found", status_code=404)

    user = update_user_db(session, user, user_in)
    return UserOut.model_validate(user)


@app.delete("/users/{user_id}")
async def delete_user(session: SessionDep, user_id: int):
    """update user"""
    user = get_user_by_id(session, user_id)
    if not user:
        raise HTTPException(detail="User not found", status_code=404)

    delete_user_db(session, user)
    return {}
