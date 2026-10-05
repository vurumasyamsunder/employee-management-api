from fastapi import FastAPI

from app.database import create_db_and_tables
from app.routers.employee import router as employee_router
from app.schemas.employee import EmployeeCreate

app = FastAPI(
    title="Employee Management API"
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(employee_router)
