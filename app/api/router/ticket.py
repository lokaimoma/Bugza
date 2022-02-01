# Created by Kelvin_Clark on 2/1/2022, 12:24 PM
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED

from app.api.dependencies.oauth import get_current_user
from app.data import get_sync_session
from app.data.schema.pydantic.comment import CommentOut, CommentIn
from app.data.schema.pydantic.ticket import TicketOut, TicketIn
from app.data.schema.pydantic.user import UserOut
from app.data.usecases.insert.insert_comment import insert_comment
from app.data.usecases.insert.insert_ticket import insert_ticket

router = APIRouter(prefix="/ticket", tags=["Tickets"])


@router.post(path="/create", status_code=HTTP_201_CREATED, response_model=TicketOut)
async def create_ticket(ticket: TicketIn, _: UserOut = Depends(get_current_user),
                        session: Session = Depends(get_sync_session)):
    ticket = insert_ticket(session=session, ticket=ticket)
    return ticket


@router.post(path="/comment", status_code=HTTP_201_CREATED, response_model=CommentOut)
async def create_comment(comment: CommentIn, session: Session = Depends(get_sync_session),
                         _: UserOut = Depends(get_current_user)):
    comment = insert_comment(comment=comment, session=session)
    return comment
