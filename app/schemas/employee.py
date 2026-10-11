from sqlmodel import SQLModel

class EmployeeCreate(SQLModel):
    name:str
    role:str
    salary:float
    department_id: int | None = None

class EmployeeResponse(SQLModel):
    id:int
    name:str
    role:str
    salary:float
    department_id: int | None = None
