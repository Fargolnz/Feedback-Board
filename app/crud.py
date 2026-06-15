from .models import Feedback

def create_feedback(db, title, message):
    feedback = Feedback(
        title=title,
        message=message
    )

    db.add(feedback)
    db.commit()
    db.refresh(feedback)

    return feedback


def get_all_feedbacks(db):
    return(
        db.query(Feedback)
        .order_by(Feedback.created_at.desc())
        .all()
    )


def update_feedback_status(db, feedback_id, status):
    feedback = (
        db.query(Feedback)
        .filter(Feedback.id == feedback_id)
        .first()
    )

    if feedback:
        feedback.status = status
        db.commit()
        db.refresh(feedback)
        
    return feedback