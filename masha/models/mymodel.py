from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    img = Column(Text, default='')
