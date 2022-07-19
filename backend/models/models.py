from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):  # User
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)  # PK
    name = Column(String(255), index=True)
    gender = Column(String(255), index=True)
    age_range = Column(String(255), index=True)
    phone_num = Column(Integer)
    created_date = Column(Integer)


class Menu(Base):  # 메뉴 테이블 생성
    __tablename__ = "menus"

    menu_id = Column(Integer, primary_key=True, index=True)
    menu_name = Column(String(255), index=True)
    menu_cost = Column(Integer)
    menu_photo_url = Column(String(2083))


class Category(Base):  # 가게 카테고리
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, index=True)  # PK
    category_name = Column(String(255), index=True)


class Store(Base):  # 가게 카테고리
    __tablename__ = "store"

    store_id = Column(Integer, primary_key=True, index=True)  # PK


class Customer(Base):  # Customer
    __tablename__ = "Customers"

    customer_id = Column(Integer, primary_key=True, index=True)  # PK
    user_id = Column(Integer, ForeignKey(User.user_id), index=True)  # FK1


class Order(Base):  # 메뉴 주문하기
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)  # PK
    customer_id = Column(Integer, ForeignKey(
        Customer.customer_id), index=True)  # FK1
    store_id = Column(Integer, ForeignKey(Store.store_id), index=True)  # FK2
    order_datetime = Column(Integer)
    order_is_takeout = Column(Boolean)
    order_cost = Column(Integer)


class Merchant(Base):  # Merchant
    __tablename__ = "merchants"

    merchant_id = Column(Integer, primary_key=True, index=True)  # PK
    user_id = Column(Integer, ForeignKey(User.user_id), index=True)  # FK1
