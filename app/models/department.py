from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
   from app.models.employee import Employee

class Department(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    employees: list["Employee"] = Relationship(back_populates="department")

