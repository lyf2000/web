from fastapi import FastAPI, Request

from db import SessionLocal
from models import User
from schema import UserSchema


app = FastAPI()


@app.get("/")
async def index(request: Request):
    return {}


@app.get("/users")
async def users(request: Request) -> list[UserSchema]:
    """user list"""

    session = SessionLocal()
    with session.begin():
        return [UserSchema(id=user.id, email=user.email) for user in session.query(User).all()]
