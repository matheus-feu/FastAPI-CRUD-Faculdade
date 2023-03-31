from typing import Optional

from pydantic import BaseModel as SCBaseModel


class CourseSchema(SCBaseModel):
    """Classe Pydantic para a entidade Curso, os dados em formato JSON são recebidos e validados
    por esta classe, são convertidos e enviados para a classe CursoModel do SQLAlchemy"""

    id: Optional[int]
    titulo: str
    descricao: str
    aulas: int
    horas: int

    class Config:
        orm_mode = True
