from datetime import datetime, timedelta
import random

from app.db.database import SessionLocal
from app.models.product import Product

db = SessionLocal()

categories = [
    "Electronics",
    "Clothing",
    "Books",
    "Sports",
    "Home",
    "Beauty"
]

batch = []

for i in range(200000):
    batch.append(
        Product(
            name=f"Product {i+1}",
            category=random.choice(categories),
            price=round(random.uniform(100, 5000), 2),
            created_at=datetime.now() - timedelta(days=random.randint(0, 365)),
            updated_at=datetime.now()
        )
    )

    if len(batch) == 5000:
        db.bulk_save_objects(batch)
        db.commit()
        batch = []
        print(f"Inserted {i+1}")

if batch:
    db.bulk_save_objects(batch)
    db.commit()

db.close()

print("Done")