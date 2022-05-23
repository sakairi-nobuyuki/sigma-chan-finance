# coding: utf-8

from typing import Union
import os
from sqlalchemy.orm import sessionmaker
import sqlalchemy
import sqlalchemy.ext.declarative

from db.models import InferenceResultsModel

from db.settings import Engine, Base


class DatabaseOperation:
    def __init__(self):
        self.session = sessionmaker(bind=Engine)()
        
        Base.metadata.create_all(bind=Engine)
        print("DB session started.")

    def __del__(self):
        self.session.close()
        print("DB session closed.")

    def insert(self, res: Base):
        """Insert data to the DB. Data shall be given in the form of DB model."""
        self.session.add(instance=res)
        self.session.commit()

    def load_inference_results_model(self, res: dict) -> InferenceResultsModel:
        if not isinstance(res, dict):
            raise Exception("Input for database insert must be dict.")
        if not self._validate_model(res):
            raise KeyError("DB model unmatch")

        return InferenceResultsModel(
            type = res["type"],
            name = res["name"],
            value = res["value"],
            source = res["source"]
        )

    def _validate_model(self, inp: dict) -> None:
        input_model_key = inp.keys()
        db_model_key = self._get_columns()

        return set(list(input_model_key)+list(["created", "modified", "id"])) == set(db_model_key)

    def _get_columns(self) -> list:
        """Get columns of the table."""
        inspector = sqlalchemy.inspect(Engine)
        columns = inspector.get_columns("inference results")

        column_name_list = [column["name"] for column in columns]

        return column_name_list
        