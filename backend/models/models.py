from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(25), unique=True, index=True)
    hashed_password = Column(String(25))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    description = Column(String(255), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


class Menu(Base):  # 메뉴 테이블 생성
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    cost = Column(Integer)
    photo_url = Column(String(2083))


class Orders(Base):  # 메뉴 주문하기
    __tablename__ = "orders"

    customer_id = Column(Integer, primary_key=True, index=True)  # PK
    store_id = Column(Integer, primary_key=True, index=True)  # PK
    order_datetime = Column(String(255))
    order_is_takeout = Column(Boolean)
    order_cost = Column(Integer)
