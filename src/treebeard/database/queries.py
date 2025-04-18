import uuid
from typing import Sequence

from leaflock.sqlalchemy_tables.textbook import Textbook
from sqlalchemy import select
from sqlalchemy.orm import Session

from treebeard.database.chat import Chat
from treebeard.database.user import Authorizer, User


def all_textbooks(session: Session) -> Sequence[Textbook]:
    return session.scalars(select(Textbook)).all()


def get_textbook(session: Session, guid: uuid.UUID) -> Textbook:
    textbook = session.get(entity=Textbook, ident=guid)

    if textbook is None:
        raise ValueError(f"No Textbook with GUID: {guid} found!")

    return textbook


def get_chat(session: Session, guid: uuid.UUID) -> Chat | None:
    return session.get(entity=Chat, ident=guid)


def get_user(session: Session, email: str, authorizer: Authorizer | str) -> User | None:
    return session.scalar(
        select(User).where(User.email == email and User.authorizer == authorizer)
    )
