from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'Obinna Ofomah',
    'retry_delay': timedelta(hours=1)
}


def greet_name(name, age):
    print(f'my name is {name} and my age is {age}')


with DAG(
    dag_id='my_first_dag',
    description='This is my first dag',
    start_date=datetime(2025,5,9,2), # OR we can use the timedelta(days=2) ie every three days 
    schedule_interval='@daily',
    default_args=default_args
) as dag:
    
    task_1 = BashOperator(
        task_id='greet_world',
        bash_command='echo Hello World, Obinna'
    )

    task_2 = PythonOperator(
        task_id='greet_me',
        python_callable=greet_name,
        op_kwargs={'name': 'Obinna', 'age': '36'}
    )