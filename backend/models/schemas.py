from decimal import Decimal
import string
from typing import List, Union
from pydantic import BaseModel
from sqlalchemy.types import TIMESTAMP

# juwon_user


class UserBase(BaseModel):
    user_id: int

    class Config:
        orm_mode = True


class User(UserBase):
    name: str
    gender: str
    age_range: str
    phone_num: str
    # created_at: str
    # updated_at: str
    # is_active: str


class UserCreate(User):
    pass


class UserRead(User):
    pass


class UserDelete(User):
    pass

# juwon_customer


class CustomerBase(BaseModel):

    class Config:
        orm_mode = True


class Customer(CustomerBase):
    user_id: int
    customer_id: int


class CustomerCreate(CustomerBase):
    pass


class CustomerRead(CustomerBase):
    pass


class CustomerDelete(Customer):
    pass

# juwon_merchant


class MerchantBase(BaseModel):

    class Config:
        orm_mode = True


class Merchant(MerchantBase):
    user_id: int
    merchant_id: int


class MerchantCreate(MerchantBase):
    pass


class MerchantRead(MerchantBase):
    pass


class MerchantDelete(Merchant):
    pass

# hyun_Menu


class MenuBase(BaseModel):  # Menu클래스들의 근간
    id: int


class MenuCreate(MenuBase):  # post
    name: str
    cost: int
    photo_url: str


class MenuRead(MenuCreate):  # get
    pass


class MenuUpdate(MenuBase):  # put
    cost: int


class MenuDelete(MenuBase):  # delete
    pass


class Menu(MenuBase):  # menu table 값들을 다 넣어줌
    name: str
    cost: int
    photo_url: str
    # created_at: str
    # updated_at: str

    class Config:
        orm_mode = True

# juwon_category


class CategoryBase(BaseModel):
    category_name: string

    class Config:
        orm_mode = True


class Category(CategoryBase):
    user_id: int


class CategoryCreate(CategoryBase):
    pass


class CategoryRead(CategoryBase):
    pass


class CategoryDelete(CategoryBase):
    pass

# juwon_location


class LocationBase(BaseModel):
    latitude: Decimal
    longitude: Decimal

    class Config:
        orm_mode = True


class Location(LocationBase):
    user_id: int


class LocationCreate(LocationBase):
    pass


class LocationRead(LocationBase):
    pass


class LocationDelete(LocationBase):
    pass

# juwon_order


class OrderBase(BaseModel):
    order_id: int
    customer_id: int
    store_id: int

    class Config:
        orm_mode = True


class Order(OrderBase):
    order_datetime: int
    order_is_takeout: bool
    order_cost: int


class OrderCreate(Order):
    pass


class OrderRead(Order):
    pass


class OrderDelete(Order):
    pass

# 추가
# s3s는 따로 안만들어도 ㄱㅊ // 그럼 s3는 함수에서 url경로 넣고 작성
