from fastapi import FastAPI, Query, Form
from fight import fight
from utils import create_fighter
import json

APP = FastAPI()
CHAR_TYPES = ["warrior", "knight", "defender", "vampire", "lancer", "healer"]


@APP.get("/")
def root():
    return {"message": "Hello World"}


@APP.post("/")
def choose(
        fighter_1=Query("warrior", enum=CHAR_TYPES),
        fighter_1_name=Form(default="John"),
        fighter_2=Query("warrior", enum=CHAR_TYPES),
        fighter_2_name=Form(default="Joe")):
    fighter_1 = create_fighter(char_type=fighter_1, char_name=fighter_1_name)
    fighter_2 = create_fighter(char_type=fighter_2, char_name=fighter_2_name)
    result = fight(fighter_1, fighter_2, False)
    return json.dumps(result)
