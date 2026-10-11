from sqlmodel import SQLModel

class DepartmentCreate(SQLModel):
    name:str
