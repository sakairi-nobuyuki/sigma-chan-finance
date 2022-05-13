from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
 
# Engine の作成
path = "sqlite:///db.sqlite3"
#path = "mysql+pymysql://root:@127.0.0.1:3306/alembic_sample"
Engine = create_engine(
  path,
  encoding="utf-8",
  echo=False
)
Base = declarative_base()


