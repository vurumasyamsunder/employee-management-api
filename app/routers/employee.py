
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.database import get_session
from app.schemas.employee import EmployeeCreate
from app.schemas.department import DepartmentCreate
from app.models.employee import Employee
from app.models.department import Department

employeerouter = APIRouter(
    prefix="/employee",
    tags=["Employees"]
)


# 1. Create Employee
@employeerouter.post("/create_employee")
def create_employee(
    employee_data: EmployeeCreate,
    session: Session = Depends(get_session)
):
    if employee_data.department_id is not None:
        department = session.get(
            Department,
            employee_data.department_id
        )

        if department is None:
            raise HTTPException(
                status_code=404,
                detail="Department not found"
            )

    employee = Employee(
        name=employee_data.name,
        role=employee_data.role,
        salary=employee_data.salary,
        department_id=employee_data.department_id
    )

    session.add(employee)
    session.commit()
    session.refresh(employee)

    return employee


# 2. Get All Employees
@employeerouter.get("/")
def get_employees(
    session: Session = Depends(get_session)
):
    statement = select(Employee)
    return session.exec(statement).all()


# 3. Get Employees with Department
# Keep this BEFORE /{employee_id}
@employeerouter.get("/with-department")
def get_employees_with_department(
    session: Session = Depends(get_session)
):
    statement = (
        select(Employee, Department)
        .join(
            Department,
            Employee.department_id == Department.id,
            isouter=True
        )
    )

    results = session.exec(statement).all()

    return [
        {
            "id": employee.id,
            "name": employee.name,
            "role": employee.role,
            "salary": employee.salary,
            "department_id": employee.department_id,
            "department_name": (
                department.name if department else None
            )
        }
        for employee, department in results
    ]


# 4. Get Employee by ID
@employeerouter.get("/{employee_id}")
def get_employee(
    employee_id: int,
    session: Session = Depends(get_session)
):
    employee = session.get(Employee, employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


# 5. Update Employee
@employeerouter.put("/{employee_id}")
def update_employee(
    employee_id: int,
    employee_data: EmployeeCreate,
    session: Session = Depends(get_session)
):
    employee = session.get(Employee, employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    if employee_data.department_id is not None:
        department = session.get(
            Department,
            employee_data.department_id
        )

        if department is None:
            raise HTTPException(
                status_code=404,
                detail="Department not found"
            )

    employee.name = employee_data.name
    employee.role = employee_data.role
    employee.salary = employee_data.salary
    employee.department_id = employee_data.department_id

    session.add(employee)
    session.commit()
    session.refresh(employee)

    return employee


# 6. Delete Employee
@employeerouter.delete("/{employee_id}")
def delete_employee(
    employee_id: int,
    session: Session = Depends(get_session)
):
    employee = session.get(Employee, employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    session.delete(employee)
    session.commit()

    return {"message": "Employee deleted successfully"}
