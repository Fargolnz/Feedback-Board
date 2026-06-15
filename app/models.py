from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime

from datetime import datetime
from .database import Base

class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True)

    title = Column(String(255), nullable=False)

    message = Column(Text, nullable=False)

    status = Column(
        String(50),
        default="registered"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )