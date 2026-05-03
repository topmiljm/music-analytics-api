import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # ← key line

def run_sql_file(relative_path):
    full_path = os.path.join(BASE_DIR, relative_path)

    with open(full_path, 'r', encoding='utf-8') as f:
        sql = f.read()

    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

    print(f"{relative_path} executed successfully!")

if __name__ == "__main__":
    run_sql_file("sql/schema.sql")
    run_sql_file("sql/seed.sql")