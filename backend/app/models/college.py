from sqlalchemy import Column, Integer, String

from app.database.base import Base


class College(Base):
    __tablename__ = "colleges"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    code = Column(String(20), unique=True, nullable=False)
    email = Column(String(100))
    phone = Column(String(20))
    address = Column(String(300))