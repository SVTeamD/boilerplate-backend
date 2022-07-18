from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from models import crud, models, schemas
from models.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


########################################

@app.post("/menus/", response_model = schemas.Menu) # menu_id는 누가 입력할지 -> 사장 or 자동
def create_menu_info(menu: schemas.MenuCreate, db: Session = Depends(get_db)):
    return crud.create_menuinfo(db, name = menu.menu_name)


@app.get("/menus/", response_model=List[schemas.Menu])
def read_menu_info(skip: int = 1, limit: int = 1000000, db: Session = Depends(get_db)):
    menus = crud.get_menuinfo(db, skip=skip, limit=limit)
    return menus


# @app.post("/users/{menu_id}/menus/", response_model = schemas.Menu) # menu_id는 누가 입력할지 -> 사장 or 자동
# def create_menu_info(menu: schemas.MenuCreate, db: Session = Depends(get_db)):
#     return crud.create_menuinfo(db, name = menu.menu_name) #이게모지?
    


# @app.get("/users/{menu_id}/informations/", response_model = schemas.Menu) # 가게이름 검색시 메뉴정보 get
# def get_search_menu_info(menu: schemas.MenuRead, db: Session = Depends(get_db)):
#     search_menu = crud.get_search_menuinfo(db, skip = skip, limit = limit)
#     return search_menu
