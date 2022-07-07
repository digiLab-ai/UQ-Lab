from fastapi import FastAPI, File, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from . import settings


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return settings.templates.TemplateResponse(
        "pages/homepage.html", {"request": request}
    )
