from sqlalchemy.orm import Session

from . import models, schemas


#############################################################################


# def get_orderinfo(db: Session, order_id: str):
#     return db.query(models.Order).filter(models.User.email == order_id).first()


# def create_order(db: Session, order: schemas.OrderCreate):
#     db_order = models.User(email=order.dict())
#     db.add(db_order)
#     db.commit()
#     db.refresh(db_order)
#     return db_order


# def delete_order(db: Session, order: schemas.OrderDelete):
#     ...
# 사용자가 주문 확인할떄 주문내역 보여줌
def get_order(db: Session, skip: int = 1, limit: int = 10):
    return db.query(models.Order).offset(skip).limit(limit).all()


# 사용자가 주문페이지로 가면 주문 정보를 자동으로 보여줌 + 업주 측 페이지로 주문 접수시 필요
def get_order_by_id(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.order_id == order_id).first()


# 사용자가 입력한 정보들을 order 테이블에 json형식으로 넣어줌
def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(customer_id=order.customer_id, store_id=order.store_id,
                            order_datetime=order.order_datetime, order_is_takeout=order.order_is_takeout, order_cost=order.order_cost)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def delete_order(db: Session, order_id: int):  # 사용자가 order id를 삭제하면 주문내역 삭제됨
    order = db.query(models.Order).filter_by(
        models.Order.order_id == order_id).first()
    db.delete(order)
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)
