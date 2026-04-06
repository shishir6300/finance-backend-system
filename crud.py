from sqlalchemy.orm import Session
import models, schemas

def create_record(db: Session, record: schemas.RecordCreate):
    db_record = models.FinancialRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def get_records(db: Session, filters: dict = None):
    query = db.query(models.FinancialRecord)

    if filters:
        if filters.get("type"):
            query = query.filter(models.FinancialRecord.type == filters["type"])
        if filters.get("category"):
            query = query.filter(models.FinancialRecord.category == filters["category"])

    return query.all()

def get_record(db: Session, record_id: int):
    return db.query(models.FinancialRecord).filter(models.FinancialRecord.id == record_id).first()

def update_record(db: Session, record_id: int, data: schemas.RecordUpdate):
    record = get_record(db, record_id)
    if not record:
        return None

    for key, value in data.dict(exclude_unset=True).items():
        setattr(record, key, value)

    db.commit()
    db.refresh(record)
    return record

def delete_record(db: Session, record_id: int):
    record = get_record(db, record_id)
    if not record:
        return None

    db.delete(record)
    db.commit()
    return record

def get_summary(db: Session):
    records = db.query(models.FinancialRecord).all()

    income = sum(r.amount for r in records if r.type == "income")
    expense = sum(r.amount for r in records if r.type == "expense")

    return {
        "total_income": income,
        "total_expense": expense,
        "balance": income - expense
    }

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
