# Created by Kelvin_Clark on 2/2/2022, 2:13 AM
from typing import List, Optional

from sqlalchemy import select, func, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.data.entities.ticket import Ticket
from app.data.enum.ticket_type import TicketType
from app.data.enum.ticket_state import TicketState
from app.data.schema.pydantic.ticket import TicketSummary
from app.utils.constants import ROWS_PER_PAGE


async def get_tickets_by_project_id(session: AsyncSession, project_id: int) -> List[Ticket]:
    query = select(Ticket).where(Ticket.project_id == project_id)
    result = await session.execute(query)
    return result.scalars().all()


async def get_tickets(session: AsyncSession, page_number: int) -> List[Ticket]:
    query = select(Ticket).limit(ROWS_PER_PAGE).offset(ROWS_PER_PAGE * page_number)
    result = await session.execute(query)
    return result.scalars().all()


async def get_ticket_by_id(session: AsyncSession, ticket_id: int) -> Optional[Ticket]:
    query = select(Ticket).where(Ticket.id == ticket_id)
    result = await session.execute(query)
    return result.scalar_one_or_none()


async def get_latest_tickets(session: AsyncSession, count: Optional[int] = 5) -> List[Ticket]:
    query = select(Ticket).limit(count).order_by(Ticket.id.desc())
    result = await session.execute(query)
    return result.scalars().all()


async def get_tickets_summary(session: AsyncSession) -> TicketSummary:
    query = select(func.count(Ticket.id))
    total = await session.execute(query)
    total = total.scalar_one()
    query = select(func.count(Ticket.id)).where(
        and_(Ticket.type == TicketType.FEATURE_REQUEST, Ticket.state == TicketState.OPEN))
    feature_count = await session.execute(query)
    feature_count = feature_count.scalar_one()
    query = select(func.count(Ticket.id)).where(Ticket.state == TicketState.OPEN)
    _open = await session.execute(query)
    _open = _open.scalar_one()
    return TicketSummary(total_tickets=total,
                         closed=total - _open,
                         open=_open,
                         open_feature_request=feature_count,
                         open_issues=_open - feature_count)
