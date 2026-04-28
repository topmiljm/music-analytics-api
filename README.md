# 🎵 Music Analytics API

## 📌 Overview

A backend REST API built with FastAPI and PostgreSQL that tracks music listening activity and provides analytics such as top tracks, artists, genres, and listening trends.

This project focuses on **data-driven backend design**, using raw SQL for analytics and a modular architecture for scalability.

---

## 🚀 Features

* User, artist, and track management
* Listening history tracking
* Analytics endpoints powered by SQL:

  * Top tracks per user
  * Top artists and genres
  * Global popular tracks and artists
  * Daily listening activity
* Modular SQL query system (separate `.sql` files)
* Clean REST API structure

---

## 🛠 Tech Stack

* Python
* FastAPI
* PostgreSQL
* psycopg2

---

## 🏗 Architecture

```
app/
├── main.py              # FastAPI entry point
├── db.py                # Database connection
├── routes/              # API endpoints
├── analytics.py         # SQL execution layer
├── sql/
│   ├── schema.sql       # Database schema
│   ├── seed.sql         # Seed data
│   └── analytics/       # Analytics queries
```

### Key Design Decisions

* **SQL-first analytics**
  Complex queries are written in dedicated `.sql` files instead of inline Python.

* **Separation of concerns**

  * Routes handle HTTP logic
  * SQL files handle data logic
  * Python handles orchestration

* **Scalable structure**
  New analytics features can be added by simply creating new SQL files and endpoints.

---

## ▶️ Running Locally

### 1. Clone the repo

```
git clone https://github.com/topmiljm/music-analytics-api.git
cd music-analytics-api
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Set up PostgreSQL

Create a database:

```
createdb music_db
```

Run schema + seed scripts:

```
python app/load_sql.py
```

### 5. Start the server

```
uvicorn app.main:app --reload
```

API available at:

```
http://127.0.0.1:8000/docs
```

---

## 📡 Example Endpoints

### Create User

```
POST /users
```

### Create Track

```
POST /tracks
```

### Record Listening

```
POST /listening
```

### User Top Tracks

```
GET /analytics/users/{user_id}/top-tracks
```

### Popular Tracks

```
GET /analytics/popular-tracks
```

---

## 📊 Example Response

```json
[
  {
    "track_id": 4,
    "title": "Around the World",
    "plays": 12,
    "total_seconds": 1800
  }
]
```

---

## 🔮 Future Improvements

* JWT authentication
* Pagination (`limit` / `offset`)
* Caching for analytics queries
* Deployment (Render / Docker)
* Role-based access control

---

## 💡 What This Project Demonstrates

* REST API design
* Relational database modeling
* SQL analytics (JOIN, GROUP BY, aggregation)
* Backend architecture and separation of concerns
* Debugging and error handling

---

## 📬 Author

Built by James T.
