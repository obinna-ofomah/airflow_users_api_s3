import requests
import pandas
import boto3
import awswrangler as wr
from airflow.models import Variable


def extract_data():
    url = 'https://randomuser.me/api/?results=10'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()['results']
        return data
    else:
        print('Unresponsive Server')


def transform_data(ti):
    first_name = []
    last_name = []
    country = []
    age = []

    list_object = ti.xcom_pull(task_ids='extract_data')

    for user in list_object:
        first_name.append(user['name']['first'])
        last_name.append(user['name']['last'])
        country.append(user['location']['country'])
        age.append(user['dob']['age'])
    users_details = {
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'country': country
    }

    return users_details


def load_data(ti):
    transformed_data = ti.xcom_pull(task_ids='transform_data')
    df = pandas.DataFrame(transformed_data)

    session = boto3.Session(aws_access_key_id=Variable.get('Access'),
                            aws_secret_access_key=Variable.get('Secret'),
                            region_name=Variable.get('region')
                            )
    file_name = 'random_user_data.parquet'
    folder_name = 'users_data_folder'
    bucket = 'obinna-api-projects'
    path = f's3://{bucket}/{folder_name}/{file_name}'

    wr.s3.to_parquet(
        df=df,
        path=path,
        dataset=True,
        mode='append',
        boto3_session=session
    )
