import datetime

from sqlalchemy import Column, Integer, String, DateTime

from app.db.base_model import Base


class CourseModel(Base):
    """Classe do SQLAlchemy para a tabela cursos, que herda de Base Declarative, sendo a classe responsável
    por criar a tabela cursos no banco de dados, orientação a objetos."""
    __tablename__ = "cursos"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(100))
    descricao: str = Column(String(255))
    aulas: int = Column(Integer)
    horas: int = Column(Integer)

    data_criacao = Column(DateTime, default=datetime.datetime.utcnow())
    data_alteracao = Column(DateTime, default=datetime.datetime.utcnow(), onupdate=datetime.datetime.utcnow())
