from fastapi import FastAPI
from .routers import customers
from .database import Base, engine

# Crée les tables (comme EF Core Migrations)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart ETL API",
    description="Migration .NET → Python IA-ready",
    version="1.0.0"
)

app.include_router(customers.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenue dans ton API IA-ready !"}