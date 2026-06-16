from fastapi import APIRouter
from fastapi import Request
from fastapi import Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from .database import SessionLocal
from .crud import (
    create_feedback,
    get_all_feedbacks,
    update_feedback_status
)

router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)


@router.get("/")
def feedback_page(request: Request):

    return templates.TemplateResponse(
        "feedback.html",
        {
            "request": request,
            "page": "feedback"
        }
    )


@router.post("/feedback")
def submit_feedback(
    title: str = Form(...),
    message: str = Form(...)
):

    db = SessionLocal()

    try:
        create_feedback(
            db=db,
            title=title,
            message=message
        )

    finally:
        db.close()

    return RedirectResponse(
        url="/",
        status_code=303
    )


@router.get("/login")
def login_page(request: Request):

    return templates.TemplateResponse(
        "login.html",
        {
            "request": request,
            "error": False
        }
    )


@router.post("/login")
def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):

    if (
        username == "admin"
        and
        password == "verystrongpass"
    ):

        request.session["admin"] = username

        return RedirectResponse(
            "/dashboard",
            status_code=303
        )

    return templates.TemplateResponse(
        "login.html",
        {
            "request": request,
            "error": True
        }
    )


@router.get("/logout")
def logout(request: Request):

    request.session.clear()

    return RedirectResponse(
        "/",
        status_code=303
    )


@router.get("/dashboard")
def dashboard_page(request: Request):

    if not request.session.get("admin"):
        return RedirectResponse(
            "/login",
            status_code=303
        )

    db = SessionLocal()

    try:
        feedbacks = get_all_feedbacks(db)

    finally:
        db.close()

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "feedbacks": feedbacks
        }
    )


@router.post("/feedback/{feedback_id}/status")
def change_feedback_status(
    feedback_id: int,
    status: str = Form(...)
):

    db = SessionLocal()

    try:
        update_feedback_status(
            db=db,
            feedback_id=feedback_id,
            status=status
        )

    finally:
        db.close()

    return RedirectResponse(
        url="/dashboard",
        status_code=303
    )