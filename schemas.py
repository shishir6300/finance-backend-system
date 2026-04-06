from pydantic import BaseModel
from datetime import date
from typing import Optional

class RecordBase(BaseModel):
    amount: float
    type: str
    category: str
    date: date
    notes: Optional[str] = None

class RecordCreate(RecordBase):
    pass

class RecordUpdate(BaseModel):
    amount: Optional[float]
    type: Optional[str]
    category: Optional[str]
    date: Optional[date]
    notes: Optional[str]

class RecordOut(RecordBase):
    id: int

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    username: str
    role: str

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True
