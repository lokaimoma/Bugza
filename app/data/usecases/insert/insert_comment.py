# Created by Kelvin_Clark on 2/1/2022, 11:02 PM
from sqlalchemy.orm import Session

from app.data.entities.comments import Comment
from app.data.schema.pydantic.comment import CommentIn


def insert_comment(comment: CommentIn, session: Session) -> Comment:
    comment = Comment(user_id=comment.user_id, ticket_id=comment.ticket_id, text=comment.text)
    session.add(comment)
    session.commit()
    session.refresh(comment)
    return comment
