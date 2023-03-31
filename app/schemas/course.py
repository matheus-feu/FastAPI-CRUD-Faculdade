from typing import Optional

from pydantic import BaseModel, validator


class CourseSchema(BaseModel):
    """Classe Pydantic para a entidade Curso, os dados em formato JSON são recebidos e validados
    por esta classe, são convertidos e enviados para a classe CursoModel do SQLAlchemy"""

    id: Optional[int]
    titulo: str
    descricao: str
    aulas: int
    horas: int

    class Config:
        orm_mode = True

    @validator('titulo')
    def validar_titulo(cls, value: str):

        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O título deve ter pelo menos 3 palavras.')

        if value.islower():
            raise ValueError('O título deve iniciar com letras maiúsculas. (Capitalizado)')

        return value

    @validator("aulas")
    def validar_aulas(cls, value):
        if value < 5:
            raise ValueError('O curso deve ter mais de 5 aulas.')
        return value

    @validator('horas')
    def validar_horas(cls, value: int):
        if value < 10:
            raise ValueError('O curso deve ter mais de 10 horas.')
        return value
