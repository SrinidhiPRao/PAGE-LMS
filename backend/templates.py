from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter()

templates = Jinja2Templates(directory="frontend")


@router.get("/signup", response_class=HTMLResponse)
def get_signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


@router.get("/login", response_class=HTMLResponse)
def get_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/personality", response_class=HTMLResponse)
def get_personality_page(request: Request):
    return templates.TemplateResponse("personality.html", {"request": request})
