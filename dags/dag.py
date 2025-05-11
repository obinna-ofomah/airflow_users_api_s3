from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from etl_pipeline import *


default_args = {
    'owner': 'Obinna Ofomah',
    'start_date': datetime(2025, 5, 8, 2),
    'schedule_interval': '@daily',
    'retries': 3
}

etl_dag = DAG(
    dag_id='etl_pipeline',
    default_args=default_args
)

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=etl_dag
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=etl_dag
)

load_task =  PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=etl_dag
)


extract_task >> transform_task >> load_task