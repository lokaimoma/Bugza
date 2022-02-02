# Created by Kelvin_Clark on 2/2/2022, 2:17 AM
from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.data.entities.comments import Comment
from app.utils.constants import ROWS_PER_PAGE


async def get_comments_by_ticket_id(session: AsyncSession, offset: int, ticket_id) -> List[Comment]:
    query = select(Comment).where(Comment.ticket_id == ticket_id).limit(ROWS_PER_PAGE).offset(offset * ROWS_PER_PAGE)
    result = await session.execute(query)
    return result.scalars().all()
