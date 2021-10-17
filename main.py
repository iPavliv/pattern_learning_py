import uvicorn
from fight import fight
from utils import create_fighter
from fastapi import FastAPI, Body, Request, Form, Depends
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

APP = FastAPI()
CHAR_TYPES = ["warrior", "knight", "defender", "vampire", "lancer", "healer"]
APP.mount("/static", StaticFiles(directory="static"), name="static")
TEMPLATES = Jinja2Templates(directory="templates")


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


@APP.get("/", response_class=HTMLResponse)
def root(request: Request):
    return TEMPLATES.TemplateResponse("fight_set.html", {"request": request})


@APP.post("/", response_class=HTMLResponse)
def start_fight(
        request: Request,
        #fighter_1: CharModel = Body(default=CharModel(char_name="John", char_type="warrior")),
        fighter_1: CharModel = Depends(Fighter1.as_form),
        #fighter_2: CharModel = Body(default=CharModel(char_name="Joe", char_type="warrior")),
        fighter_2: CharModel = Depends(Fighter2.as_form),
):
    fighter_1 = create_fighter(fighter_1)
    fighter_2 = create_fighter(fighter_2)
    result = fight(fighter_1, fighter_2)
    return TEMPLATES.TemplateResponse("fight_set.html", {
        "request": request, "messages": result
    })


if __name__ == "__main__":
    uvicorn.run(APP)
