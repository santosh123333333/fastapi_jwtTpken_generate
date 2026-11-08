from datetime import datetime, timezone

from sqlalchemy import String,DateTime,Integer
from sqlalchemy.orm import Mapped,mapped_column

from app.db.database import Base




class User(Base):
    __tablename__="users"

    id:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    full_name:Mapped[String]=mapped_column(String(200),nullable=False)
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )
    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
    default=lambda: datetime.now(timezone.utc),
    nullable=False
)