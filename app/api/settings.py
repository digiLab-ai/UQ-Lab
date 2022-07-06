from fastapi.templating import Jinja2Templates
import os


APP_DIR = "app"
TEMPLATES_DIR = os.path.join(APP_DIR, "templates")
PLUGIN_DIR = os.path.join(TEMPLATES_DIR, "plugins")
STATIC_DIR = os.path.join(APP_DIR, "static")
RESOURCES_DIR = os.path.join(STATIC_DIR, "resources")

if not os.path.isdir(RESOURCES_DIR):
    os.mkdir(RESOURCES_DIR)


templates = Jinja2Templates(directory=TEMPLATES_DIR)
