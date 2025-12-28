from uuid import UUID
from datetime import datetime

from sqlalchemy import String, ForeignKey, text
from sqlalchemy import UUID as PG_UUID
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    """Base class for all models."""

    pass


class Project(Base):
    """Project model."""

    __tablename__ = "projects"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=text("gen_random_uuid()")
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(1024), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )

    tasks: Mapped[list["Task"]] = relationship(
        "Task",
        back_populates="project",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    documents: Mapped[list["Document"]] = relationship(
        "Document",
        back_populates="project",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )


class Task(Base):
    """Task model."""

    __tablename__ = "tasks"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=text("gen_random_uuid()")
    )
    project_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=True)
    priority: Mapped[int] = mapped_column(nullable=False, default=0)
    status: Mapped[int] = mapped_column(nullable=False, default=0)
    duedate: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )

    project: Mapped["Project"] = relationship(
        "Project",
        back_populates="tasks",
    )


class Document(Base):
    """Document model."""

    __tablename__ = "documents"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=text("gen_random_uuid()")
    )
    project_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )

    project: Mapped["Project"] = relationship(
        "Project",
        back_populates="documents",
    )