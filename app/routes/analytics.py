from fastapi import APIRouter, HTTPException
from app.analytics import run_query

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

# Mapping of endpoints → SQL filenames
ENDPOINTS = {
    "users/{user_id}/top-tracks": "user_top_tracks.sql",
    "users/{user_id}/top-artists": "user_top_artists.sql",
    "users/{user_id}/top-genres": "user_top_genres.sql",
    "users/{user_id}/daily-listening": "daily_listening.sql",
    "popular-tracks": "popular_tracks.sql",
    "popular-artists": "popular_artists.sql",
    "genre-listening": "genre_listening_time.sql",
}

# Dynamically create endpoints
for path, sql_file in ENDPOINTS.items():
    async def endpoint(user_id: int = None, limit: int = 10, sql_file=sql_file):
        params = {"user_id": user_id, "limit": limit} if user_id else {"limit": limit}
        try:
            rows = run_query(sql_file, params)
            return [dict(zip([desc[0] for desc in rows.description], r)) for r in rows]
        except FileNotFoundError as e:
            raise HTTPException(status_code=404, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    router.add_api_route(f"/{path}", endpoint, methods=["GET"])


# @router.get("/users/{user_id}/top-tracks")
# def user_top_tracks(user_id: int, limit: int = 10):
#     rows = run_query(
#         "sql/analytics/user_top_tracks.sql",
#         {"user_id": user_id, "limit": limit}
#     )

#     return [
#         {
#             "track_id": r[0],
#             "title": r[1],
#             "plays": r[2],
#             "total_seconds": r[3],
#         }
#         for r in rows
#     ]

# @router.get("/users/{user_id}/top-artists")
# def user_top_artists(user_id: int, limit: int = 10):
#     rows = run_query(
#         "sql/analytics/user_top_artists.sql",
#         {"user_id": user_id, "limit": limit}
#     )
#     return [
#         {
#             "artist_id": r[0],
#             "name": r[1],
#             "plays": r[2],
#             "total_seconds": r[3],
#         }
#         for r in rows
#     ]

# @router.get("/popular-tracks")
# def popular_tracks(limit: int = 10):
#     rows = run_query(
#         "sql/analytics/popular_tracks.sql",
#         {"limit": limit}
#     )
#     return [
#         {
#             "track_id": r[0],
#             "title": r[1],
#             "plays": r[2],
#             "total_seconds": r[3],
#         }
#         for r in rows
#     ]

# @router.get("/listening/genres")
# def genre_listening_time():
#     rows = run_query("sql/analytics/genre_listening_time.sql")
#     return [
#         {
#             "genre_id": r[0],
#             "name": r[1],
#             "total_seconds": r[2],
#         }
#         for r in rows
#     ]

# @router.get("/users/{user_id}/daily-listening")
# def user_daily_listening(user_id: int):
#     rows = run_query(
#         "sql/analytics/daily_listening.sql",
#         {"user_id": user_id}
#     )
#     return [
#         {
#             "day": r[0].isoformat(),
#             "total_seconds": r[1],
#             "plays": r[2],
#         }
#         for r in rows
#     ]

# @router.get("/users/{user_id}/daily-listening")
# def user_daily_listening(user_id: int):
#     rows = run_query(
#         "sql/analytics/daily_listening.sql",
#         {"user_id": user_id}
#     )
#     return [
#         {
#             "day": r[0].isoformat(),
#             "total_seconds": r[1],
#             "plays": r[2],
#         }
#         for r in rows
#     ]

# @router.get("/popular-artists")
# def popular_artists(limit: int = 10):
#     rows = run_query(
#         "sql/analytics/popular_artists.sql",
#         {"limit": limit}
#     )
#     return [
#         {
#             "artist_id": r[0],
#             "name": r[1],
#             "plays": r[2],
#             "total_seconds": r[3],
#         }
#         for r in rows
#     ]

# @router.get("/users/{user_id}/top-genres")
# def user_top_genres(user_id: int, limit: int = 10):
#     rows = run_query(
#         "sql/analytics/user_top_genres.sql",
#         {"user_id": user_id, "limit": limit}
#     )
#     return [
#         {
#             "genre_id": r[0],
#             "name": r[1],
#             "plays": r[2],
#             "total_seconds": r[3],
#         }
#         for r in rows
#     ]