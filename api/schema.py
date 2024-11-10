from pydantic import BaseModel, ConfigDict, EmailStr


class SqlSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class UserBaseSchema(SqlSchema):
    email: EmailStr


class UserIn(UserBaseSchema):
    pass


class UserOut(UserBaseSchema):
    id: int
