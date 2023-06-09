import logging

from app.db.base_model import Base
from app.db.database import engine

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)


async def create_tables() -> None:
    """Cria as tabelas no banco de dados."""
    import app.models.__all_models  # noqa: F401
    logging.info("Criando tabelas...")

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)  # Exclua caso já exista
        await conn.run_sync(Base.metadata.create_all)  # Cria as tabelas
    logging.info("Tabelas criadas com sucesso!")


if __name__ == "__main__":
    import asyncio

    asyncio.run(create_tables())
