from fastapi import FastAPI

app=FastAPI(title="python show fastapi",description="Employee Management API",version="1.0.0")

@app.get("/")
def home():
    return {
        "Employee Management System built with FastAPI"
    }