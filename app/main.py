from fastapi import FastAPI
from fastapi import Request
from fastapi import Form
from fastapi.responses import RedirectResponse

from fastapi.templating import Jinja2Templates

from .database import Base
from .database import engine
from .database import SessionLocal

from .crud import create_feedback
from .crud import get_all_feedbacks
from .crud import update_status

app = FastAPI()

Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(
    directory="app/templates"
)

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "create_feedback.html",
        {
            "request": request
        }
    )

@app.post("/feedback")
def submit_feedback(
        title: str = Form(...),
        message: str = Form(...)
):

    db = SessionLocal()

    create_feedback(
        db,
        title,
        message
    )

    return RedirectResponse(
        "/",
        status_code=303
    )

@app.get("/dashboard")
def dashboard(request: Request):
    db = SessionLocal()

    feedbacks = get_all_feedbacks(db)

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "feedbacks": feedbacks
        }
    )

@app.post("/feedback/{feedback_id}/status")
def change_status(
        feedback_id: int,
        status: str = Form(...)
):

    db = SessionLocal()

    update_status(
        db,
        feedback_id,
        status
    )

    return RedirectResponse(
        "/dashboard",
        status_code=303
    )