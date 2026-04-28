import os
import psycopg2
from app.db import get_connection

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQL_DIR = os.path.join(BASE_DIR, "sql", "analytics")

def run_query(sql_file, params=None):
    full_path = os.path.join(SQL_DIR, sql_file)
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"SQL file not found: {full_path}")

    with open(full_path, "r", encoding="utf-8") as f:
        query = f.read()

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, params or {})
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows