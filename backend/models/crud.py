from sqlalchemy.orm import Session

from . import models, schemas

# User ############################################################################


def get_user(db: Session, skip: int = 1, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(user_id=user.user_id,
                          name=user.name,
                          gender=user.gender,
                          age_range=user.age_range,
                          phone_num=user.phone_num
                          )
    db.add(db_user)
    db.commit()
    return db_user


def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter_by(
        models.User.user_id == user_id).first()
    db.delete(user)
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

# Customer ############################################################################


def get_customer(db: Session, skip: int = 1, limit: int = 10):
    return db.query(models.Customer).offset(skip).limit(limit).all()


def get_customer_by_id(db: Session, user_id: int):
    return db.query(models.Customer).filter(models.Customer.user_id == user_id).first()


def create_customer(db: Session, customer: schemas.CustomerCreate, user_id):
    db_user = db.query(models.User).filter(
        models.User.user_id == user_id).first()
    db_customer = models.Customer(user_id=db_user.user_id)
    db.add(db_customer)
    db.commit()
    return db_customer


def delete_customer(db: Session, customer_id: int):
    customer = db.query(models.customer).filter_by(
        models.Customer.customer_id == customer_id).first()
    db.delete(customer)
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

# Merchant ############################################################################


def get_merchant(db: Session, skip: int = 1, limit: int = 10):
    return db.query(models.Merchant).offset(skip).limit(limit).all()


def get_merchant_by_id(db: Session, merchant_id: int):
    return db.query(models.Merchant).filter(models.Merchant.merchant_id == merchant_id).first()


def create_merchant(db: Session, merchant: schemas.MerchantCreate, user_id):
    db_user = db.query(models.User).filter(
        models.User.user_id == user_id).first()
    db_merchant = models.Merchant(user_id=db_user.user_id)
    db.add(db_merchant)
    db.commit()
    return db_merchant


def delete_merchant(db: Session, merchant_id: int):
    merchant = db.query(models.merchant).filter_by(
        models.Merchant.merchant_id == merchant_id).first()
    db.delete(merchant)
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

# Menu ###################################################################################


def get_menu(db: Session):  # 사용자가 메뉴정보 등록한 값들 잘 들어갔는지 보여줌
    return db.query(models.Menu).all()


def get_menu_by_id(db: Session, id: int):  # 사용자가 가게 정보페이지로 이동하면 가게 정보들을 자동으로 보여줌
    return db.query(models.Menu).filter(models.Menu.id == id).first()


def get_menu_by_name(db: Session, menu_name: str):  # 사용자가 메뉴 이름을 검색 시 가게 정보들을 보여줌
    return db.query(models.Menu).filter(models.Menu.name == menu_name).first()


# 사용자가 입력한 정보들을 menu 테이블에 json형식으로 넣어줌
def create_menu(db: Session, menu: schemas.MenuCreate):
    db_menu = models.Menu(name=menu.name, cost=menu.cost,
                          photo_url=menu.photo_url)
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu


def delete_menu(db: Session, menu_name: str):  # 사용자가 메뉴이를 삭제하면 menu 테이블들의 값들도 삭제됨
    menu = db.query(models.Menu).filter(models.Menu.name == menu_name).first()
    db.delete(menu)
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

# order ############################################################################

# 사용자가 주문 확인할떄 주문내역 전체 보여줌


def get_order(db: Session, skip: int = 1, limit: int = 10):
    return db.query(models.Order).offset(skip).limit(limit).all()


# 사용자가 주문페이지로 가면 주문 정보를 보여줌 + 업주 측 페이지로 주문 접수시 필요
def get_order_by_id(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.order_id == order_id).first()


# 사용자가 입력한 정보들을 order 테이블에 json형식으로 넣어줌
def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(customer_id=order.customer_id, store_id=order.store_id,
                            order_datetime=order.order_datetime, order_is_takeout=order.order_is_takeout, order_cost=order.order_cost)
    db.add(db_order)
    db.commit()
    # db.refresh(db_order)
    return db_order


def delete_order(db: Session, order_id: int):  # 사용자가 order id를 삭제하면 주문내역 삭제됨
    order = db.query(models.Order).filter_by(
        models.Order.order_id == order_id).first()
    db.delete(order)
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)
