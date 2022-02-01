# Created by Kelvin_Clark on 2/1/2022, 12:42 PM
from sqlalchemy.orm import Session

from app.data.entities.ticket import Ticket

from app.data.schema.pydantic.ticket import TicketIn


def insert_ticket(session: Session, ticket: TicketIn) -> Ticket:
    ticket = Ticket(project_id=ticket.project_id, creator_id=ticket.creator_id, title=ticket.title,
                    description=ticket.description, ticket_state=ticket.state, ticket_type=ticket.type)
    session.add(ticket)
    session.commit()
    session.refresh(ticket)
    return ticket
