from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime

with DAG('hello_dag', start_date=datetime(2023, 1, 1), schedule='0 14 * * *', catchup=False) as dag:

    hello_task = BashOperator(
        task_id='hello_task',
        bash_command='echo Hello'
    )