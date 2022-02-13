# Created by Kelvin_Clark on 2/2/2022, 1:18 AM
from datetime import datetime
from typing import Optional

import strawberry
from strawberry.types import Info

from app.data.entities.comments import Comment as CommentModel
from app.data.schema.gaphql.user import User
from app.data.usecases.getters.get_user import get_user_by_id
from app.utils.constants import DB_SESSION_SYNC


@strawberry.type
class Comment:
    id: int
    user_id: int
    ticket_id: int
    text: str
    date_created: str

    @strawberry.field
    def creator(self, info: Info) -> Optional[User]:
        user = get_user_by_id(session=info.context[DB_SESSION_SYNC], user_id=self.user_id)
        if user is None:
            return None
        return User(user=user)

    def __init__(self, comment: CommentModel):
        self.id = comment.id
        self.user_id = comment.user_id
        self.ticket_id = comment.ticket_id
        self.text = comment.text
        self.date_created = comment.date_created.__str__()
