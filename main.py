import uvicorn

from db import init_db, get_session
from fight import fight
from models.char_model import CharModel, Fighter1, Fighter2
from models.user_model import User
from statistics import Statistics
from utils import create_fighter
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

APP = FastAPI()
CHAR_TYPES = ["warrior", "knight", "defender", "vampire", "lancer", "healer"]
APP.mount("/static", StaticFiles(directory="static"), name="static")
TEMPLATES = Jinja2Templates(directory="templates")


@APP.on_event("startup")
async def on_startup():
    await init_db()


@APP.get("/user", response_model=User)
async def get_user(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User))
    user = result.scalars().first()
    return user


@APP.post("/user", response_model=User)
async def create_user(user: User, session: AsyncSession = Depends(get_session)):
    new_user = User(name=user.name, surname=user.surname)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user


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
    stats = Statistics()
    # stats.increase_score - to improve (and move) statistic increase
    return TEMPLATES.TemplateResponse("fight_set.html", {
        "request": request, "messages": result
    })


if __name__ == "__main__":
    uvicorn.run(APP)
