from curses import is_term_resized
from unicodedata import name
from fastapi import Response
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT
import datetime
from . import models, schemas



 

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

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
