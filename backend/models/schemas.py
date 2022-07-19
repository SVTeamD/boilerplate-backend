from typing import List, Union
<<<<<<< main
<<<<<<< main
=======
from xmlrpc.client import boolean
=======
>>>>>>> feat: write order_api and change models.py's order

>>>>>>> feat: order_api schemas
from pydantic import BaseModel
from sqlalchemy.types import TIMESTAMP

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


<<<<<<< main


###############추가
### s3s는 따로 안만들어도 ㄱㅊ // 그럼 s3는 함수에서 url경로 넣고 작성
class MenuBase(BaseModel): # Menu클래스들의 근간
    # id: int
    ...

class MenuCreate(MenuBase): # post
    name: str
    cost: int
    photo_url: str

class MenuRead(MenuCreate): # get
    pass
class MenuUpdate(MenuBase): # put
    cost: int

class MenuDelete(MenuBase): # delete
    pass

class Menu(MenuBase): # menu table 값들을 다 넣어줌
    name: str
    cost: int
    photo_url: str
    # created_at: str
    # updated_at: str

    class Config:
        orm_mode = True


=======
# juwon
class OrderBase(BaseModel):
    order_id: int
    customer_id: int
    store_id: int


class Order(OrderBase):
    order_datetime: int
    order_is_takeout: bool
    order_cost: int

    class Config:
        orm_mode = True


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
>>>>>>> feat: order_api schemas
