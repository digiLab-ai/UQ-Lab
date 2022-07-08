from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from . import settings
from . import database


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/validate_credentials/{username}/{password}")
async def validate_credentials(username: str, password: str):
    return database.validate_credentials(username, password)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return settings.templates.TemplateResponse(
        "pages/overview.html",
        {"request": request, "campaign_names": database.get_campaign_names()},
    )


@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return settings.templates.TemplateResponse(
        "pages/login.html",
        {"request": request},
    )


@app.get("/campaign", response_class=HTMLResponse)
async def campaign(request: Request):
    return settings.templates.TemplateResponse(
        "pages/campaign.html", {"request": request}
    )
