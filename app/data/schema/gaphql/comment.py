# Created by Kelvin_Clark on 2/2/2022, 1:18 AM
import strawberry

from app.data.entities.comments import Comment as CommentModel
from app.data.schema.gaphql.user import User


@strawberry.type
class Comment:
    id: int
    user_id: int
    ticket_id: int
    text: str

    instance: strawberry.Private[CommentModel]

    @strawberry.field
    def user(self) -> User:
        return User(user=self.instance.user)

    def __init__(self, comment: CommentModel):
        self.id = comment.id
        self.user_id = comment.user_id
        self.ticket_id = comment.ticket_id
        self.text = comment.text
        self.instance = comment
