from fastapi import APIRouter, HTTPException
from app.db import get_connection

router = APIRouter(
    prefix="/listening",
    tags=["Listening"]
)

@router.post("/")
def record_listen(user_id: int, track_id: int, seconds: int):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            INSERT INTO listening_history (user_id, track_id, listen_seconds)
            VALUES (%s, %s, %s);
            """,
            (user_id, track_id, seconds)
        )
        conn.commit()
    except Exception:
        conn.rollback()
        raise HTTPException(
            status_code=400,
            detail="Invalid user_id or track_id"
        )
    finally:
        cur.close()
        conn.close()

    return {"status": "listening recorded"}