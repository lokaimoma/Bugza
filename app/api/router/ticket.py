# Created by Kelvin_Clark on 2/1/2022, 12:24 PM
from typing import List, Optional

from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED

from app.api.dependencies.oauth import get_current_user
from app.data import get_sync_session, get_async_session
from app.data.schema.pydantic.comment import CommentOut, CommentIn, CommentCount
from app.data.schema.pydantic.ticket import TicketOut, TicketIn, TicketSummary
from app.data.schema.pydantic.user import UserOut
from app.data.usecases.getters.get_ticket import get_latest_tickets, get_tickets_summary
from app.data.usecases.getters.get_comment import get_total_comments_by_ticket_id
from app.data.usecases.insert.insert_comment import insert_comment
from app.data.usecases.insert.insert_ticket import insert_ticket
from app.connection_manager import connection_manager

router = APIRouter(prefix="/ticket", tags=["Tickets"])


@router.post(path="/create", status_code=HTTP_201_CREATED, response_model=TicketOut)
async def create_ticket(ticket: TicketIn, _: UserOut = Depends(get_current_user),
                        session: Session = Depends(get_sync_session)):
    ticket = insert_ticket(session=session, ticket=ticket)
    return ticket


@router.post(path="/comment", status_code=HTTP_201_CREATED, response_model=CommentOut)
async def create_comment(comment: CommentIn, background_task: BackgroundTasks,
                         session: Session = Depends(get_sync_session),
                         _: UserOut = Depends(get_current_user)):
    comment = insert_comment(comment=comment, session=session)
    background_task.add_task(connection_manager.broadcast_to_channel, f"ticket_{comment.ticket_id}_comments_channel",
                             CommentOut(**comment.__dict__).dict())
    return comment


@router.get(path="/latest", response_model=List[TicketOut])
async def _get_latest_tickets(count: Optional[int] = 5, session: AsyncSession = Depends(get_async_session),
                              _: UserOut = Depends(get_current_user)):
    tickets = await get_latest_tickets(session=session, count=count)
    return tickets


@router.get(path="/summary", response_model=TicketSummary)
async def _get_tickets_summary(session: AsyncSession = Depends(get_async_session),
                               _: UserOut = Depends(get_current_user)):
    summary = await get_tickets_summary(session=session)
    return summary


@router.get(path="/comment_count", response_model=CommentCount)
async def _get_total_comments_count(ticket_id: int, session: AsyncSession = Depends(get_async_session)):
    comment_count = await get_total_comments_by_ticket_id(session=session, ticket_id=ticket_id)
    return comment_count
