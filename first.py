import pprint

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG;



print("this is an example");


# Operators; we need this to operate!
#from airflow.operators.bash_operator import BashOperator
from airflow.operators.bash_operator import BashOperator

#from datetime import datetime, timedelta
from datetime import datetime, timedelta;

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

default_args = {
    'owner': 'airfloww',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'email': ['anthony.mcclay@me.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

