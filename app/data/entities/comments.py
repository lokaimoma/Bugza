# Created by Kelvin_Clark on 1/30/2022, 10:33 PM
import sqlalchemy as sa

from app.data import SQLALCHEMY_BASE


class Comment(SQLALCHEMY_BASE):
    __tablename__ = "comments"
    id: int = sa.Column(sa.BIGINT, primary_key=True, autoincrement=True)
    user_id: int = sa.Column(sa.BIGINT, sa.ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"),
                             nullable=False)
    ticket_id: int = sa.Column(sa.BIGINT, sa.ForeignKey("tickets.id", onupdate="CASCADE", ondelete="CASCADE"),
                               nullable=False)
    text: str = sa.Column(sa.TEXT, nullable=False)

    def __init__(self, user_id: int, ticket_id: int, text: str):
        self.user_id = user_id
        self.ticket_id = ticket_id
        self.text = text