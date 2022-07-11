from fastapi import APIRouter, Depends
from pathlib import Path
from pydantic import BaseModel
import atexit
import copy
import json
import os

from . import settings
from .auth import manager


database_route = APIRouter()


def load_books():
    book_names = [f.name for f in os.scandir(settings.BOOKS_DIR) if f.is_dir()]

    books = {}
    for name in book_names:
        book_dir = os.path.join(settings.BOOKS_DIR, name)
        books[name] = json.loads(Path(os.path.join(book_dir, "meta.json")).read_text())

    return books


DB = json.loads(Path(settings.DATABASE_PATH).read_text())
DB["books"] = load_books()


def exit_handler():
    del DB["books"]
    Path(settings.DATABASE_PATH).write_text(json.dumps(DB, indent=4))


atexit.register(exit_handler)


@database_route.get("/books")
async def books(user=Depends(manager)):
    books = copy.deepcopy(DB["books"])

    for name in books:
        books[name]["owned"] = name in user["owned_books"]

    return books


class PurchaseOrder(BaseModel):
    name: str


@database_route.post("/purchase_book")
async def purchase_book(order: PurchaseOrder, user=Depends(manager)):
    if order.name not in user["owned_books"]:
        user["owned_books"].append(order.name)
