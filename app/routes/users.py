from fastapi import APIRouter, HTTPException
from app.db import get_connection

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/")
def create_user(email: str, display_name: str):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            INSERT INTO users (email, display_name)
            VALUES (%s, %s)
            RETURNING id;
            """,
            (email, display_name)
        )
        user_id = cur.fetchone()[0]
        conn.commit()
    except Exception:
        conn.rollback()
        raise HTTPException(status_code=400, detail="User already exists")
    finally:
        cur.close()
        conn.close()

    return {"id": user_id, "email": email, "display_name": display_name}


@router.get("/{user_id}")
def get_user(user_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, email, display_name FROM users WHERE id=%s;",
        (user_id,)
    )
    row = cur.fetchone()

    cur.close()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="User not found")

    return {"id": row[0], "email": row[1], "display_name": row[2]}