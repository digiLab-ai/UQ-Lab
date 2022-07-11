from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from . import settings
from .auth import auth_route
from .components import components_route


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(auth_route, prefix="/auth")
app.include_router(components_route, prefix="/components")


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return settings.templates.TemplateResponse(
        "pages/overview.html", {"request": request}
    )


@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return settings.templates.TemplateResponse("pages/login.html", {"request": request})


@app.get("/campaign/{name}", response_class=HTMLResponse)
async def login(request: Request, name: str):
    return settings.templates.TemplateResponse(
        "pages/campaign.html", {"request": request, "campaign_name": name}
    )
