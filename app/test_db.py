from app.db import get_connection

try:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    print("Connection successful:", cur.fetchone())
    cur.close()
    conn.close()
except Exception as e:
    print("Connection failed:", e)