from typing import List
from unicodedata import name

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

# juwon_user


@app.post("/users/", response_model=schemas.User)
def create_user_info(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user=user)


@app.get("/users/{user_id}/")
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    users = crud.get_user_by_id(db, user_id=user_id)
    return users


@app.delete("/users/{name}/")
def delete_user_by_name(name: str, db: Session = Depends(get_db)):
    response = crud.delete_user(db, name=name)
    return response.status_code

# juwon_customer


@app.post("/customers/{user_id}", response_model=schemas.Customer)
def create_customer_info(customer: schemas.CustomerCreate, user_id, db: Session = Depends(get_db)):
    return crud.create_customer(db, user_id=user_id, customer=customer)


@app.get("/customers/{user_id}/")
def read_customer_by_id(user_id: int, db: Session = Depends(get_db)):
    customers = crud.get_customer_by_id(db, user_id=user_id)
    return customers


@app.delete("/customers/delete/{customer_id}/")
def delete_customer_by_id(customer_id: str, db: Session = Depends(get_db)):
    response = crud.delete_customer(db, customer_id=customer_id)
    return response.status_code

# juwon_merchant


@app.post("/merchants/{user_id}", response_model=schemas.Merchant)
def create_merchant_info(merchant: schemas.MerchantCreate, user_id, db: Session = Depends(get_db)):
    return crud.create_merchant(db, user_id=user_id, merchant=merchant)


@app.get("/merchants/{user_id}/")
def read_merchant_by_id(user_id: int, db: Session = Depends(get_db)):
    merchants = crud.get_merchant_by_id(db, user_id=user_id)
    return merchants


@app.delete("/merchants/delete/{merchant_id}/")
def delete_merchant_by_id(merchant_id: str, db: Session = Depends(get_db)):
    response = crud.delete_merchant(db, merchant_id=merchant_id)
    return response.status_code

# hyun_menu
# menu_id는 누가 입력할지 -> 사장 or 자동


@app.post("/menus/", response_model=schemas.Menu)
def create_menu_info(menu: schemas.MenuCreate, db: Session = Depends(get_db)):
    return crud.create_menu(db, menu=menu)


@app.get("/menus/", response_model=List[schemas.Menu])
def read_menu_info(skip: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    menus = crud.get_menu(db)
    return menus


@app.get("/menus/{id}/")
def read_menu_by_id(id: int, db: Session = Depends(get_db)):
    menus = crud.get_menu_by_id(db, id=id)
    return menus


@app.get("/menus/name/{menu_name}/")
def read_menu_by_name(menu_name: str, db: Session = Depends(get_db)):
    menus = crud.get_menu_by_name(db, menu_name=menu_name)
    return menus


@app.delete("/menus/{menu_name}/")
def delete_menu_by_name(menu_name: str, db: Session = Depends(get_db)):
    response = crud.delete_menu(db, menu_name=menu_name)
    return response.status_code

# juwon_category


@app.post("/category/", response_model=schemas.Category)
def create_order_info(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order=order)


@app.get("/category/{category_id}/")
def read_order_by_id(order_id: int, db: Session = Depends(get_db)):
    orders = crud.get_order_by_id(db, order_id=order_id)
    return orders


@app.delete("/category/{category_id}/")
def delete_order_by_name(order_id: int, db: Session = Depends(get_db)):
    response = crud.delete_order(db, order_id=order_id)
    return response.status_code

# juwon_location


@app.post("/orders/", response_model=schemas.Order)
def create_order_info(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order=order)


@app.get("/orders/{order_id}/")
def read_order_by_id(order_id: int, db: Session = Depends(get_db)):
    orders = crud.get_order_by_id(db, order_id=order_id)
    return orders


@app.delete("/orders/{order_id}/")
def delete_order_by_name(order_id: int, db: Session = Depends(get_db)):
    response = crud.delete_order(db, order_id=order_id)
    return response.status_code

# juwon_order


@app.post("/orders/", response_model=schemas.Order)
def create_order_info(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order=order)


@app.get("/orders/{order_id}/")
def read_order_by_id(order_id: int, db: Session = Depends(get_db)):
    orders = crud.get_order_by_id(db, order_id=order_id)
    return orders


@app.delete("/orders/{order_id}/")
def delete_order_by_name(order_id: int, db: Session = Depends(get_db)):
    response = crud.delete_order(db, order_id=order_id)
    return response.status_code
