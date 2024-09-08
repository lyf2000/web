from pydantic import BaseModel, ConfigDict


class SqlSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class UserBaseSchema(SqlSchema):
    email: str


class UserIn(UserBaseSchema):
    pass


class UserOut(UserBaseSchema):
    id: int
