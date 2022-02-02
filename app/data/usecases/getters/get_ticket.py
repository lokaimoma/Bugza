# Created by Kelvin_Clark on 2/2/2022, 2:13 AM
from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.data.entities.ticket import Ticket
from app.utils.constants import ROWS_PER_PAGE


async def get_tickets(session: AsyncSession, page_number: int) -> List[Ticket]:
    query = select(Ticket).limit(ROWS_PER_PAGE).offset(ROWS_PER_PAGE * page_number)
    result = await session.execute(query)
    return result.scalars().all()


async def get_ticket_by_id(session: AsyncSession, ticket_id: int) -> Optional[Ticket]:
    query = select(Ticket).where(Ticket.id == ticket_id)
    result = await session.execute(query)
    return result.scalar_one_or_none()
