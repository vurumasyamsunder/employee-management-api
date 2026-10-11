from fastapi import APIRouter,Depends,HTTPException
from sqlmodel import Session,select

from app.database import get_session
from app.models.department import Department
from app.models.employee import Employee
from app.schemas.department import DepartmentCreate



departmentrouter=APIRouter(prefix="/department",tags=["Departments"])

@departmentrouter.post("/create_employee")

# GET ALL DEPARTMENTS
@departmentrouter.get("/ALLdepartments")
def get_departments(session: Session = Depends(get_session)):
    departments = session.exec(select(Department)).all()
    return departments

# GET DEPARTMENT BY ID
@departmentrouter.get("/{department_id}")
def get_department(department_id:int,session:Session=Depends(get_session)):
    department=session.get(Department,department_id)
    if department is None:
        raise HTTPException(status_code=404,detail="Department not found")
    return department


# UPDATE DEPARTMENT
@departmentrouter.put("/department/{department_id}")
def update_department(department_id:int,department_data:DepartmentCreate,session:Session=Depends(get_session)):
    department=session.get(Department,department_id)

    if department is None:
        raise HTTPException(status_code=404,detail="Department not found")
    department.name=department_data.name

    session.add(department)
    session.commit()
    session.refresh(department)

    return department


# CREATE DEPARTMENT
@departmentrouter.post("/create_department")
def create_department(department_data:DepartmentCreate,session:Session=Depends(get_session)):
    print("name",department_data.name)
    department=Department(name=department_data.name)

    session.add(department)
    session.commit()
    session.refresh(department)
    return department

