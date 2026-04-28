import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

# Connect to default database to create new one
conn = psycopg2.connect(
    dbname="postgres",
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cur = conn.cursor()

# Create database if it doesn't exist
cur.execute(f"SELECT 1 FROM pg_database WHERE datname='{DB_NAME}'")
exists = cur.fetchone()
if not exists:
    cur.execute(f'CREATE DATABASE {DB_NAME};')
    print(f"Database '{DB_NAME}' created successfully!")
else:
    print(f"Database '{DB_NAME}' already exists.")

cur.close()
conn.close()