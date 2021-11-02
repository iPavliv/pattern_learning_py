import uvicorn
from fight import fight
from models.char_model import CharModel, Fighter1, Fighter2
from utils import create_fighter
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

APP = FastAPI()
CHAR_TYPES = ["warrior", "knight", "defender", "vampire", "lancer", "healer"]
APP.mount("/static", StaticFiles(directory="static"), name="static")
TEMPLATES = Jinja2Templates(directory="templates")


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
