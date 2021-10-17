from fight import fight
from utils import create_fighter
from fastapi import FastAPI, Body
from pydantic import BaseModel

APP = FastAPI()
CHAR_TYPES = ["warrior", "knight", "defender", "vampire", "lancer", "healer"]


class CharModel(BaseModel):
    char_name: str
    char_type: str


@APP.get("/")
def root():
    return {"message": "Hello World"}


@APP.post("/")
def start_fight(
        fighter_1: CharModel = Body(default=CharModel(char_name="John", char_type="warrior")),
        fighter_2: CharModel = Body(default=CharModel(char_name="Joe", char_type="warrior"))
):
    fighter_1 = create_fighter(fighter_1)
    fighter_2 = create_fighter(fighter_2)
    result = fight(fighter_1, fighter_2)
    return result
