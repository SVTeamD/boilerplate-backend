from typing import List, Union
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




###############추가
### s3s는 따로 안만들어도 ㄱㅊ // 그럼 s3는 함수에서 url경로 넣고 작성
class MenuBase(BaseModel): # Menu클래스들의 근간
    menu_id: int

class MenuCreate(MenuBase): # post
    menu_name: str
    menu_cost: int
    menu_photo_url: str

class MenuRead(MenuCreate): # get
    pass
class MenuUpdate(MenuBase): # put
    menu_cost: int

class MenuDelete(MenuBase): # delete
    pass

class Menu(MenuBase): # menu table 값들을 다 넣어줌
    menu_name: str
    menu_cost: int
    menu_photo_url: str
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True


