from sqlmodel import SQLModel,Field,Relationship
from typing import Optional

class Department(SQLModel,table=True):
    id:int |None=Field(default=None,primary_key=True)
    name:str
    employees:list["Employee"]=Relationship(back_populates="department")
class Employee(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    name:str
    role:str
    salary:float
    department_id:int=Field(foreign_key="department.id")
    department:Department=Relationship(back_populates="employees")

