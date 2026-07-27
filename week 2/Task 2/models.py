from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import uuid
from sqlalchemy import UUID


class Base(DeclarativeBase):
    pass

class Task(Base):
    __tablename__="task"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    title:Mapped[str]
    done:Mapped[bool] = mapped_column(default=False)


