# ETL Pipeline for Random User Data

This project implements an **ETL (Extract, Transform, Load)** pipeline using Apache Airflow. The pipeline fetches random user data from a public API, transforms the relevant fields, and loads the data into an S3 bucket in Parquet format. This process runs on a daily schedule.

## ✨ Features

- **Extraction** of 10 random users from [randomuser.me](https://randomuser.me)
- **Transformation** to select relevant fields: first name, last name, age, and country
- **Loading** of structured data into Amazon S3 in columnar Parquet format
- Containerised using Docker for deployment
- Designed using **Apache Airflow** for orchestration and scheduling
- Uses **Boto3** and **awswrangler** for seamless AWS integration

---

## 📁 Project Structure

```text
.
├── etl_pipeline.py     # Contains the ETL logic: extract, transform, and load functions
├── dag_definition.py   # Defines the Airflow DAG and tasks
├── README.md           # Project documentation
