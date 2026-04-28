# Music Analytics API

## Overview
Backend API built with FastAPI and PostgreSQL to track music listening activity and generate analytics.

## Features
- Users, artists, tracks, listening history
- Analytics endpoints (top tracks, artists, genres)
- Raw SQL queries for data analysis
- Modular project structure

## Tech Stack
- Python
- FastAPI
- PostgreSQL

## Running Locally

```bash
uvicorn app.main:app --reload


# API will be available at:
# http://127.0.0.1:8000/docs

# Example Endpoints
# GET /artists
# POST /users
# POST /tracks
# GET /analytics/users/{user_id}/top-tracks
# Notes

# This project is being actively developed and will include:

# JWT authentication
# Pagination
# Caching