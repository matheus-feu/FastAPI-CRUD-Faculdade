from typing import List

from fastapi import status, Depends, APIRouter, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_session
from app.models.course import CourseModel
from app.schemas.course import CourseSchema

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CourseSchema)
async def post_course(course: CourseSchema, db: AsyncSession = Depends(get_session)):
    """Envia JSON e espera receber JSON, inserir no banco e retornar o JSON inserido
    POST Curso - Insere um curso no banco de dados"""
    new_course: CourseModel = CourseModel(titulo=course.titulo,
                                          descricao=course.descricao,
                                          aulas=course.aulas,
                                          horas=course.horas)
    db.add(new_course)
    await db.commit()

    return new_course


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[CourseSchema])
async def get_courses(db: AsyncSession = Depends(get_session)):
    """GET Cursos - Retorna todos os cursos do banco de dados"""
    async with db as session:
        query = select(CourseModel)
        result = await session.execute(query)
        courses: List[CourseModel] = result.scalars().unique().all()

        return courses


@router.get("/{curso_id}", status_code=status.HTTP_200_OK, response_model=CourseSchema)
async def get_course_id(curso_id: int, db: AsyncSession = Depends(get_session)):
    """GET Curso - Retorna um curso do banco de dados"""
    async with db as session:
        query = select(CourseModel).where(CourseModel.id == curso_id)
        result = await session.execute(query)
        course: CourseModel = result.scalar_one_or_none()  # Ou trás um curso ou trás None

        if course:
            return course
        else:
            HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

        return course


@router.put("/{curso_id}", status_code=status.HTTP_200_OK, response_model=CourseSchema)
async def put_course_id(curso_id: int, course: CourseSchema, db: AsyncSession = Depends(get_session)):
    """PUT Curso - Atualiza um curso no banco de dados"""
    async with db as session:
        query = select(CourseModel).where(CourseModel.id == curso_id)
        result = await session.execute(query)
        course_up: CourseModel = result.scalars().unique().one_or_none()

        # Verifica se o curso existe, se existir atualiza os dados
        if course_up:
            if course.titulo:
                course_up.titulo = course.titulo
            if course.descricao:
                course_up.descricao = course.descricao
            if course.aulas:
                course_up.aulas = course.aulas
            if course.horas:
                course_up.horas = course.horas

            await session.commit()

            return course_up
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")


@router.delete("/{curso_id}", status_code=status.HTTP_200_OK, response_model=CourseSchema)
async def delete_course_id(curso_id: int, db: AsyncSession = Depends(get_session)):
    """DELETE Curso - Deleta um curso do banco de dados"""
    async with db as session:
        query = select(CourseModel).where(CourseModel.id == curso_id)
        result = await session.execute(query)
        course_del: CourseModel = result.scalars().unique().one_or_none()

        if course_del:
            await session.delete(course_del)
            await session.commit()

            return course_del
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
