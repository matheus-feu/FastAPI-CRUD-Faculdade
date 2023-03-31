import logging

from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from config.settings import settings

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

logging.info("Criando engine de conexão com o banco de dados...")
engine: AsyncEngine = create_async_engine(settings.SQLALCHEMY_URI_CONN, echo=True)
logging.info("Criando sessão de conexão com o banco de dados...")

SessionLocal: AsyncSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)

