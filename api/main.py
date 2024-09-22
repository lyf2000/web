from fastapi import FastAPI, Request, Form, status
from fastapi.exceptions import HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

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


templates = Jinja2Templates(directory="templates/")

app = FastAPI()


# forms
@app.get("/", response_class=HTMLResponse)
async def index(request: Request, session: SessionDep, new_user_id=None):
    user = None
    if new_user_id:
        user = get_user_by_id(session, new_user_id)
    return templates.TemplateResponse("index.html", context={"request": request, "user_created": user})


@app.post("/", response_class=HTMLResponse)
async def form_post_create_user(request: Request, session: SessionDep):
    async with request.form() as form:
        email = form["email"]
        user = User(email=email)
        user = create_user_db(session, user)

    return RedirectResponse(url=f"/?new_user_id={user.id}", status_code=status.HTTP_303_SEE_OTHER)


# api
@app.get("/api/users")
async def users(session: SessionDep) -> list[UserOut]:
    """user list"""
    users = get_users(session)
    print(users)
    return [UserOut.model_validate(user) for user in users]


@app.get("/api/users/{user_id}")
async def get_user(session: SessionDep, user_id: int) -> UserOut:
    """get user"""
    user = get_user_by_id(session, user_id)
    if not user:
        raise HTTPException(detail="User not found", status_code=404)

    return UserOut.model_validate(user)


@app.post("/api/users")
async def create_user(session: SessionDep, user: UserIn) -> UserOut:
    """create user"""
    user = User(**user.model_dump())
    create_user_db(session, user)
    return UserOut.model_validate(user)


@app.put("/api/users/{user_id}")
async def update_user(session: SessionDep, user_id: int, user_in: UserIn) -> UserOut:
    """update user"""
    user = get_user_by_id(session, user_id)
    if not user:
        raise HTTPException(detail="User not found", status_code=404)

    user = update_user_db(session, user, user_in)
    return UserOut.model_validate(user)


@app.delete("/api/users/{user_id}")
async def delete_user(session: SessionDep, user_id: int):
    """update user"""
    user = get_user_by_id(session, user_id)
    if not user:
        raise HTTPException(detail="User not found", status_code=404)

    delete_user_db(session, user)
    return {}
