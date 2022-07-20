from decimal import Decimal
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func, text

from .database import Base


class User(Base):  # User
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)  # PK
    name = Column(String(255), index=True)
    gender = Column(String(255), index=True)
    age_range = Column(String(255), index=True)
    phone_num = Column(Integer)
    created_date = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))


class Customer(Base):  # Customer
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)  # PK
    user_id = Column(Integer, ForeignKey("users.user_id"), index=True)  # FK1


class Merchant(Base):  # Merchant
    __tablename__ = "merchants"

    merchant_id = Column(Integer, primary_key=True, index=True)  # PK
    user_id = Column(Integer, ForeignKey("users.user_id"), index=True)  # FK1


class Menu(Base):  # 메뉴 테이블 생성
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    cost = Column(Integer)
    photo_url = Column(String(2083))
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))


class Category(Base):  # 가게 카테고리
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, index=True)  # PK
    category_name = Column(String(255), index=True)


class Location(Base):  # 가게 카테고리
    __tablename__ = "locations"

    location_id = Column(Integer, primary_key=True, index=True)  # PK
    # latitude = Column(Decimal, index=True)
    # longtitude = Column(Decimal, index=True)


class Store(Base):  # 가게 카테고리
    __tablename__ = "stores"

    store_id = Column(Integer, primary_key=True, index=True)  # PK
    merchant_id = Column(Integer, ForeignKey(
        "merchants.merchant_id"), index=True)  # FK1
    id = Column(Integer, ForeignKey("menus.id"), index=True)  # FK2
    category_id = Column(Integer, ForeignKey(
        "categories.category_id"), index=True)  # FK3
    location_id = Column(Integer, ForeignKey(
        "locations.location_id"), index=True)  # FK4
    store_name = Column(String(255), index=True)
    store_photo_url = Column(String(255), index=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))


class Order(Base):  # 메뉴 주문하기
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)  # PK
    customer_id = Column(Integer, ForeignKey(
        "customers.customer_id"), index=True)  # FK1
    store_id = Column(Integer, ForeignKey(
        "stores.store_id"), index=True)  # FK2
    order_datetime = Column(Integer)
    order_is_takeout = Column(Boolean)
    order_cost = Column(Integer)
