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
    # customer_id: int

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
    merchant_id: int

    class Config:
        orm_mode = True


class Merchant(MerchantBase):
    user_id: int


class MerchantCreate(Merchant):
    pass


class MerchantRead(Merchant):
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

# juwon_order


# class OrderBase(BaseModel):
#     class Config:
#         orm_mode = True


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
