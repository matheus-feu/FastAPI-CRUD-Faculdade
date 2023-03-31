from fastapi import APIRouter
from app.api.v1.routes import course

api_router = APIRouter()

# Rota /api/v1/cursos
api_router.include_router(course.router, prefix="/cursos", tags=["cursos"])

