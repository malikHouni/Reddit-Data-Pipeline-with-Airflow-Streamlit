from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import praw
import psycopg2

def fetch_reddit_posts():
    reddit = praw.Reddit(
        client_id='',
        client_secret='',
        user_agent=''
    )

    conn = psycopg2.connect(
        host="postgres",
        database="airflow",
        user="airflow",
        password="airflow"
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS reddit_posts (
            id TEXT PRIMARY KEY,
            title TEXT,
            author TEXT,
            created_utc TIMESTAMP
        )
    """)

    for submission in reddit.subreddit("datascience").new(limit=200):
        cur.execute("""
            INSERT INTO reddit_posts (id, title, author, created_utc)
            VALUES (%s, %s, %s, to_timestamp(%s))
            ON CONFLICT (id) DO NOTHING
        """, (
            submission.id,
            submission.title,
            str(submission.author),
            submission.created_utc
        ))

    conn.commit()
    cur.close()
    conn.close()

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'fetch_reddit_posts',
    default_args=default_args,
    description='Fetch latest Reddit posts and store in Postgres',
    schedule_interval=timedelta(minutes=3),
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    fetch_task = PythonOperator(
        task_id='fetch_reddit',
        python_callable=fetch_reddit_posts
    )
