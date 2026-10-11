
from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.department import Department


class Employee(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    role: str
    salary: float

    department_id: int | None = Field(default=None,foreign_key="department.id")

    department: "Department" = Relationship(back_populates="employees")
