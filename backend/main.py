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

<<<<<<< main
########################################

@app.post("/menus/", response_model = schemas.Menu) # menu_id는 누가 입력할지 -> 사장 or 자동
def create_menu_info(menu: schemas.MenuCreate, db: Session = Depends(get_db)):
    return crud.create_menu(db, menu = menu)


@app.get("/menus/", response_model=List[schemas.Menu])
def read_menu_info(skip: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    menus = crud.get_menu(db)
    return menus


@app.get("/menus/{menu_id}/")
def read_menu_by_id(menu_id: int, db: Session = Depends(get_db)):
    menus = crud.get_menu_by_id(db, menu_id=menu_id)
    return menus


@app.get("/menus/name/{menu_name}/")
def read_menu_by_name(menu_name: str, db: Session = Depends(get_db)):
    menus = crud.get_menu_by_name(db, menu_name=menu_name)
    return menus


@app.delete("/menus/{menu_name}")
def delete_menu_by_name(menu_name: str, db: Session = Depends(get_db)):
    response = crud.delete_menu(db, menu_name = menu_name)
    return response.status_code


=======

@app.get("/users/order/", response_model=schemas.Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    order = crud.get_user(db, order_id=order_id)
    return order


@app.post("/users/order/", response_model=schemas.Order)
def create_order(
    order_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, order_id=order_id)
<<<<<<< main
>>>>>>> feat: start writing order api
=======


# juwon_order
@app.post("/orders/", response_model=schemas.Order)
def create_order_info(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order=order)


@app.get("/orders/{order_id}/", response_model=List[schemas.Order])
def read_order_info(skip: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    orders = crud.get_order(db)
    return orders
>>>>>>> feat: write order_api and change models.py's order
