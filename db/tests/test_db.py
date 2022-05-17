# coding: utf-8

import os
from sqlalchemy.orm import sessionmaker
import sqlalchemy
import sqlalchemy.ext.declarative

import configparser



from db.settings import Base
from db.models import InferenceResultsModel

class TestDataBase:
    def test_db_url(self):
        config = configparser.ConfigParser()
        config.read("alembic.ini")
        #config.read("../alembic.ini")
        ##config.read("../../db/alembic.ini")
        
        assert config["alembic"]["sqlalchemy.url"]
        assert config["alembic"]["sqlalchemy.url"] == "sqlite:///time_series_inference.db"

    def test_start_session(self):
        if os.path.exists("time_series_inference.db"):
            os.remove("time_series_inference.db")

        config = configparser.ConfigParser()
        config.read("alembic.ini")
        url = config["alembic"]["sqlalchemy.url"]

        engine = sqlalchemy.create_engine(url, echo=True)

        Base.metadata.create_all(bind=engine)

        type = "today"
        name = "USDJPY"
        value = 105.0
        source = "frex"

        ### insert
        res = InferenceResultsModel(type=type, name=name, value=value, source=source)
        session = sessionmaker(bind=engine)()
        res.print_model_by_id(res.id)
        session.add(instance=res)
        session.commit()
        session.close()
        
        res = InferenceResultsModel(type=type, name=name, value=value, source=source)
        res.print_model_by_id(res.id)
        session.add(instance=res)
        session.commit()
        session.close()

        ### select
        session = sessionmaker(bind=engine)()
        res_select_iter = session.query(InferenceResultsModel).all()
        print("length: ", len(res_select_iter))
        for res_select in res_select_iter:
            print("in db: ", res_select.id, res_select.name, res_select.created_at)

        assert res_select_iter[0].id == 1
        assert res_select_iter[-1].id == 2
        assert res_select_iter[-1].name == res_select_iter[-2].name


        ### deinit
        os.remove("time_series_inference.db")
