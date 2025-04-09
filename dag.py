from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator  # Correct import

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 12, 18),
    'depends_on_past': False,
    'email': ['skulka63@asu.edu'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('fetch_batsmenranking_stats',
          default_args=default_args,
          description='Runs an external Python script',
          schedule='@daily',  # Optional improvement
          catchup=False)

run_script_task = BashOperator(
    task_id='run_script',
    bash_command='python /home/airflow/gcs/dags/scripts/ExtractPushToGCS2.py',
    dag=dag  # Explicitly pass dag
)
