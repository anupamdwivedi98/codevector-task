# CodeVector Task

## Overview

Backend API built using FastAPI, SQLAlchemy and PostgreSQL (Supabase).

Features:

* Cursor-based pagination
* Category filtering
* PostgreSQL database
* SQLAlchemy ORM
* FastAPI REST API

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL (Supabase)
* Uvicorn

## Setup

1. Clone repository

```bash
git clone <repo-url>
cd codevector-task
```

2. Create virtual environment

```bash
python -m venv venv
```

3. Activate virtual environment

```bash
venv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Run application

```bash
uvicorn app.main:app --reload
```

## API Endpoints

### Get Products

```http
GET /products
```

### Filter by Category

```http
GET /products?category=Books
```

### Cursor Pagination

```http
GET /products?cursor=199981
```

### Combined Example

```http
GET /products?category=Books&cursor=199981
```

## Database

* PostgreSQL (Supabase)
* 200,000 seeded product records

## Author

Anupam Dwivedi
