# Smart ETL API 🚀

> Migration d'un service .NET vers **Python + FastAPI + SQL** – **prêt pour l'IA**

## Stack

- FastAPI
- SQLAlchemy
- PostgreSQL / SQL Server
- Docker
- Pydantic

## Lancer

```bash
docker build -t smart-etl .
docker run -p 8000:8000 -e DATABASE_URL=postgresql://... smart-etl
