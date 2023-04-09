from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def greet(age, ti):
    name = ti.xcom_pull(task_ids='get_name')
    print(f"Hello World! My name is {name}, "
          f"and I am {age} years old!")

def get_name():
    return 'Jerry'

with DAG(
    default_args=default_args,
    dag_id='our_dag_with_python_operator_v04',
    description='Our first dag using python operator',
    start_date=datetime(2023,4,8),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={'age': 20}
    )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )

    task2 >> task1