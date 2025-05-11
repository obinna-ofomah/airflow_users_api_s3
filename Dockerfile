FROM apache/airflow:2.5.1

WORKDIR /users_airflow

COPY requirements.txt /users_airflow

RUN pip install -r requirements.txt