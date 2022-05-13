from email.policy import default
from sqlalchemy import Column, String, DateTime, Float
from settings import Base
from datetime import datetime

class RecordModel(Base):
    __tablename__ = "record"

    type = Column(String(16), primary_key=True)
    name = Column(String(16), primary_key=True)
    value = Column(Float, nullable=False)
    source = Column(String(16), nullable=False)
    created_at = Column("created", DateTime, default=datetime.now(), nullable=False)
    modified_at = Column("modified", DateTime, default=datetime.now(), nullable=False)