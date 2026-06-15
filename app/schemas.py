from pydantic import BaseModel

class FeedbackCreate(BaseModel):
    title: str
    message: str

class FeedbackStatusUpdate(BaseModel):
    status: str