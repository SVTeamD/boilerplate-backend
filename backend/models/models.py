from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

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

    menu_id = Column(Integer, primary_key=True, index=True)
    menu_name = Column(String(255), index=True)
    menu_cost = Column(Integer)
    menu_photo_url = Column(String(2083))
    time_created_at = Column(DateTime(timezone=True), server_default=func.now())
    time_updated_at = Column(DateTime(timezone=True), onupdate=func.now())

# class Order(Base):  # 메뉴 주문하기
#     __tablename__ = "order"

#     order_id = Column(Integer, primary_key=True, index=True)  # PK
#     customer_id = Column(Integer, ForeignKey("customer_id"), index=True)  # FK1
#     store_id = Column(Integer, ForeignKey("store_id"), index=True)  # FK2
#     order_datetime = Column(Integer)
#     order_is_takeout = Column(Boolean)
#     order_cost = Column(Integer)
