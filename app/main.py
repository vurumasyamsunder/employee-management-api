
from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.models.employee import Employee
from app.models.department import Department
from app.database import create_db_and_tables
from app.routers.employee import employeerouter as employee_router
from app.routers.department import departmentrouter as department_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    # Application startup
    create_db_and_tables()

    yield

    # Application shutdown
    # Cleanup code can go here


app = FastAPI(
    title="Employee Management API",
    lifespan=lifespan
)

app.include_router(employee_router)
app.include_router(department_router)

