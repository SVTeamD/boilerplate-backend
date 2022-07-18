from typing import List, Union
from xmlrpc.client import boolean

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True


# juwon
class OrderBase(BaseModel):
    order_id: int
    customer_id: int
    store_id: int

    class Config:
        orm_mode = True


class Order(OrderBase):
    order_datetime: int
    order_is_takeout: boolean
    order_cost: int


class OrderCreate(Order):
    pass


class OrderRead(Order):
    pass


class OrderDelete(Order):
    pass

# class Order(Base):  # 메뉴 주문하기
#     __tablename__ = "orders"

#     order_id = Column(Integer, primary_key=True, index=True)  # PK
#     customer_id = Column(Integer, ForeignKey("customer_id"), index=True)  # FK1
#     store_id = Column(Integer, ForeignKey("store_id"), index=True)  # FK2
#     order_datetime = Column(Integer)
#     order_is_takeout = Column(Boolean)
#     order_cost = Column(Integer)
