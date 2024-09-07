import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from db import SessionLocal
from models import User, create_table_users
from schema import UserSchema


app = FastAPI()


@app.get("/")
async def index(request: Request):
    create_table_users()
    return RedirectResponse(url="/users")


@app.get("/users")
async def users(request: Request) -> list[UserSchema]:
    """user list"""

    session = SessionLocal()
    with session.begin():
        return [UserSchema(id=user.id, email=user.email) for user in session.query(User).all()]


if __name__ == "__main__":
    uvicorn.run(app, port=80)
