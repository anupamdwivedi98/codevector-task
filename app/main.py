from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.db.database import Base, engine, get_db
from app.models.product import Product

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "CodeVector Task Running"}


@app.get("/products")
def get_products(
    category: str | None = None,
    limit: int = Query(default=20, le=100),
    cursor: int | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(Product)

    if category:
        query = query.filter(Product.category == category)

    if cursor:
        query = query.filter(Product.id < cursor)

    products = (
        query.order_by(desc(Product.id))
        .limit(limit)
        .all()
    )

    next_cursor = None

    if products:
        next_cursor = products[-1].id

    return {
        "count": len(products),
        "next_cursor": next_cursor,
        "data": products
    }