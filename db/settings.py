from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

import os
from pathlib  import Path

import configparser


dir_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(dir_path, "alembic.ini")
config = configparser.ConfigParser()
config.read(config_path)

# Engine の作成
Engine = create_engine(
  config["alembic"]["sqlalchemy.url"],
  encoding="utf-8",
  echo=False
)
Base = declarative_base()


