from fastapi import APIRouter,Depends
from app.schemas.employee import EmployeeCreate
from sqlmodel import Session,select
from app.database import get_session
from app.models.employee import Employee

router=APIRouter(prefix="/employee",tags=["Employees"])

@router.post("/")
def create_employee(
    employee_data: EmployeeCreate,
    session: Session = Depends(get_session)
):
    employee = Employee(
        name=employee_data.name,
        role=employee_data.role,
        salary=employee_data.salary
    )

    session.add(employee)
    session.commit()
    session.refresh(employee)

    return employee



@router.get("/")
def get_employees(
    session: Session = Depends(get_session)
):
    statement = select(Employee)

    employees = session.exec(statement).all()
    print("employees",employees)
    return employees


@router.get("/{employee_id}")
def get_employee(
    employee_id: int,
    session: Session = Depends(get_session)
):
    employee = session.get(Employee, employee_id)
    print("employee",employee)
    return employee


@router.put("/{employee_id}")
def update_employee(
    employee_id: int,
    employee_data: EmployeeCreate,
    session: Session = Depends(get_session)
):
    employee = session.get(Employee, employee_id)

    employee.name = employee_data.name
    employee.role = employee_data.role
    employee.salary = employee_data.salary

    session.add(employee)
    session.commit()
    session.refresh(employee)

    return employee

@router.delete("/{employee_id}")
def delete_employee(
    employee_id: int,
    session: Session = Depends(get_session)
):
    employee = session.get(Employee, employee_id)

    session.delete(employee)
    session.commit()

    return {"message": "Employee deleted successfully"}