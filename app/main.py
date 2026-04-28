from fastapi import FastAPI
from app.routes import artists, users, tracks, listening, analytics

app = FastAPI(title="Music Backend")

app.include_router(artists.router)
app.include_router(users.router)
app.include_router(tracks.router)
app.include_router(listening.router)
app.include_router(analytics.router)

@app.get("/")
def root():
    return {"message": "Music Backend Running"}