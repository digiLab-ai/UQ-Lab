from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

from . import settings
from . import database


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/validate_credentials/{username}/{password}")
async def validate_credentials(username: str, password: str):
    return database.validate_credentials(username, password)


@app.get("/", response_class=HTMLResponse)
async def index():
    return RedirectResponse("/login")


@app.get("/overview/{username}", response_class=HTMLResponse)
async def overview(request: Request, username: str):
    return settings.templates.TemplateResponse(
        "pages/overview.html",
        {
            "request": request,
            "username": username,
            "campaign_names": database.get_campaign_names(username),
        },
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
