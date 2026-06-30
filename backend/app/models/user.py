from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
)

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    first_name = Column(String(100))

    last_name = Column(String(100))

    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    phone = Column(String(20))

    password_hash = Column(String(255))

    is_active = Column(
        Boolean,
        default=True
    )

    role_id = Column(
        Integer,
        ForeignKey("roles.id")
    )

    college_id = Column(
        Integer,
        ForeignKey("colleges.id")
    )