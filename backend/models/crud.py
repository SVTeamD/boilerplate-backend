from curses import is_term_resized
from unicodedata import name
from fastapi import Response
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT
import datetime
from . import models, schemas


<<<<<<< main

 

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

=======
#############################################################################
>>>>>>> feat: write order_api and change models.py's order


# def get_orderinfo(db: Session, order_id: str):
#     return db.query(models.Order).filter(models.User.email == order_id).first()


# def create_order(db: Session, order: schemas.OrderCreate):
#     db_order = models.User(email=order.dict())
#     db.add(db_order)
#     db.commit()
#     db.refresh(db_order)
#     return db_order


<<<<<<< main
<<<<<<< main
#################추가###################################################################

def get_menu(db: Session): # 사용자가 메뉴정보 등록한 값들 잘 들어갔는지 보여줌
    return db.query(models.Menu).all()


def get_menu_by_id(db: Session, menu_id: int): # 사용자가 가게 정보페이지로 이동하면 가게 정보들을 자동으로 보여줌
    return db.query(models.Menu).filter(models.Menu.id == menu_id).first()


def get_menu_by_name(db: Session, menu_name: str): # 사용자가 메뉴 이름을 검색 시 가게 정보들을 보여줌
    return db.query(models.Menu).filter(models.Menu.name == menu_name).first()


def create_menu(db: Session, menu: schemas.MenuCreate): # 사용자가 입력한 정보들을 menu 테이블에 json형식으로 넣어줌
    db_menu = models.Menu(name=menu.name,cost=menu.cost, photo_url=menu.photo_url)
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu



def delete_menu(db: Session, menu_name: str): # 사용자가 메뉴이를 삭제하면 menu 테이블들의 값들도 삭제됨
    menu = db.query(models.Menu).filter(models.Menu.name == menu_name).first()
    db.delete(menu)
    db.commit()
    return Response(status_code = HTTP_204_NO_CONTENT)
=======
#############################################################################
=======
# def delete_order(db: Session, order: schemas.OrderDelete):
#     ...
# 사용자가 주문 확인할떄 주문내역 보여줌
def get_order(db: Session, skip: int = 1, limit: int = 10):
    return db.query(models.Order).offset(skip).limit(limit).all()
>>>>>>> feat: write order_api and change models.py's order


# 사용자가 주문페이지로 가면 주문 정보를 자동으로 보여줌 + 업주 측 페이지로 주문 접수시 필요
def get_order_by_id(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.order_id == order_id).first()


# 사용자가 입력한 정보들을 order 테이블에 json형식으로 넣어줌
def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(customer_id=order.customer_id, store_id=order.store_id,
                            order_datetime=order.order_datetime, order_is_takeout=order.order_is_takeout, order_cost=order.order_cost)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


<<<<<<< main
def delete_order(db: Session, order: schemas.OrderDelete):
    ...
>>>>>>> feat: start writing order api
=======
def delete_order(db: Session, order_id: int):  # 사용자가 order id를 삭제하면 주문내역 삭제됨
    order = db.query(models.Order).filter_by(
        models.Order.order_id == order_id).first()
    db.delete(order)
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)
>>>>>>> feat: write order_api and change models.py's order
