from fastapi import APIRouter, HTTPException
from app.db import get_connection

router = APIRouter(
    prefix="/artists",
    tags=["Artists"]
)

# GET all artists
@router.get("/")
def get_artists():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM artists ORDER BY name;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "name": r[1]} for r in rows]


# GET artist by ID
@router.get("/{artist_id}")
def get_artist(artist_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM artists WHERE id=%s;", (artist_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if row:
        return {"id": row[0], "name": row[1]}
    else:
        raise HTTPException(status_code=404, detail="Artist not found")


# POST new artist
@router.post("/")
def create_artist(name: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO artists (name) VALUES (%s) RETURNING id;",
        (name,)
    )
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return {"id": new_id, "name": name}


# DELETE artist
@router.delete("/{artist_id}")
def delete_artist(artist_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM artists WHERE id=%s RETURNING id;",
        (artist_id,)
    )
    deleted = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    if deleted:
        return {"deleted_id": deleted[0]}
    else:
        raise HTTPException(status_code=404, detail="Artist not found")