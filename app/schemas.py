from pydantic import BaseModel, EmailStr

class CustomerBase(BaseModel):
    name: str
    email: EmailStr

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    id: int
    churn_risk: float

    class Config:
        from_attributes = True  # remplace orm_mode