import logging
from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession

from core.db.database import SessionLocal

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)


async def get_session() -> Generator:
    """ Criando uma sessão de conexão com o banco de dados, faz o uso e encerra a conexão,
    isso permite que a conexão seja reutilizada por outras requisições, sem que o banco de dados
    fique sobrecarregado. Generator: Retorna um gerador de sessão de conexão com o banco de dados."""

    logging.info("Gerando uma sessão de conexão com o banco de dados...")
    session: AsyncSession = SessionLocal()

    try:
        yield session
    finally:
        await session.close()
