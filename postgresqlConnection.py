

from sqlalchemy import create_engine
from sqlalchemy import MetaData

engine = create_engine('postgresql+psycopg2://airflow_user:11javajava@localhost:5432/airflowdb')
connection = engine.connect()


