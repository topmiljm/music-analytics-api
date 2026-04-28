from fastapi import APIRouter, HTTPException
from app.db import get_connection

router = APIRouter(
    prefix="/tracks",
    tags=["Tracks"]
)

@router.post("/")
def create_track(title: str, artist_id: int, duration_seconds: int):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            INSERT INTO tracks (title, artist_id, duration_seconds)
            VALUES (%s, %s, %s)
            RETURNING id;
            """,
            (title, artist_id, duration_seconds)
        )
        track_id = cur.fetchone()[0]
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()

    return {
        "id": track_id,
        "title": title,
        "artist_id": artist_id,
        "duration_seconds": duration_seconds
    }


@router.get("/{track_id}")
def get_track(track_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT t.id, t.title, a.name, t.duration_seconds
        FROM tracks t
        JOIN artists a ON a.id = t.artist_id
        WHERE t.id = %s;
        """,
        (track_id,)
    )
    row = cur.fetchone()

    cur.close()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Track not found")

    return {
        "id": row[0],
        "title": row[1],
        "artist": row[2],
        "duration_seconds": row[3]
    }