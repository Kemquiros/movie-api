from fastapi import APIRouter
from fastapi.responses import HTMLResponse

home_router = APIRouter()


@home_router.get(
    '/',
    tags=['home'])
def read_root():
    return HTMLResponse("<h1>Hello World!!</h1>")
