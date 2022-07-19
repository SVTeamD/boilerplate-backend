from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from models import crud, models, schemas
from models.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# juwon_Order


@app.get("/users/order/", response_model=schemas.Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    order = crud.get_user(db, order_id=order_id)
    return order


@app.post("/users/order/", response_model=schemas.Order)
def create_order(
    order_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, order_id=order_id)


# juwon_order
@app.post("/orders/", response_model=schemas.Order)
def create_order_info(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order=order)


@app.get("/orders/{order_id}/", response_model=List[schemas.Order])
def read_order_info(skip: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    orders = crud.get_order(db)
    return orders
