from fastapi import Form
from pydantic import BaseModel


class CharModel(BaseModel):
    char_name: str
    char_type: str


class Fighter1(BaseModel):
    char_name: str
    char_type: str

    @classmethod
    def as_form(
        cls,
        char_name1: str = Form(...),
        char_type1: str = Form(...)
    ):
        return cls(char_name=char_name1, char_type=char_type1)


class Fighter2(BaseModel):
    char_name: str
    char_type: str

    @classmethod
    def as_form(
        cls,
        char_name2: str = Form(...),
        char_type2: str = Form(...)
    ):
        return cls(char_name=char_name2, char_type=char_type2)
