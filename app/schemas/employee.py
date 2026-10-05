from sqlmodel import SQLModel

class EmployeeCreate(SQLModel):
    name:str
    role:str
    salary:float

class EmployeeResponse(SQLModel):
    id:int
    name:str
    role:str
    salary:float

