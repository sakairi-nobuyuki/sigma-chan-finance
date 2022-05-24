
from sqlalchemy import Column, String, DateTime, Integer, Float, Index
from db.settings import Base

from datetime import datetime

class InferenceResultsModel(Base):
    __tablename__ = "inference_results"

    id = Column(Integer, primary_key = True, autoincrement=True)
    type = Column(String(16), nullable=False)
    name = Column(String(16), nullable=False)
    value = Column(Float, nullable=False)
    source = Column(String(16), nullable=False)
    modified_at = Column("modified", DateTime, default=datetime.now(), nullable=False)
    created_at = Column("created", DateTime, default=datetime.now(), nullable=False)


    def print_model_by_id(self, id: str) -> None:
        print(f"Contents of InferenceResults of {id}")
        print(f"  id: {self.id}, type: {self.type}, name: {self.name}, value: {self.value}")