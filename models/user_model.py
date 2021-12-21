from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    name: str
    surname: str


class User(UserBase, table=True):
    id: uuid = Field(primary_key=True)
