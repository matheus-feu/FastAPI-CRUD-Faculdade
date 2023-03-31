import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """Classe de configuração gerais da aplicação, que herda de BaseSettings do pydantic."""
    APP_VERSION: str = os.getenv("APP_VERSION")
    API_V1_PREFIX: str = os.getenv("API_V1_PREFIX")

    PROJECT_NAME: str = os.getenv("PROJECT_NAME")
    PROJECT_DESCRIPTION: str = os.getenv("PROJECT_DESCRIPTION")

    DB_URI: str = os.getenv("POSTGRES_URI")
    DB_USER: str = os.getenv("POSTGRES_USER")
    DB_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    DB_HOST: str = os.getenv("POSTGRES_HOST")
    DB_PORT: str = os.getenv("POSTGRES_PORT")
    DB_NAME: str = os.getenv("POSTGRES_DB")

    # Example: mysql+aiomysql://root:root@localhost:3306/test
    SQLALCHEMY_URI_CONN: str = "{0}{1}:{2}@{3}:{4}/{5}".format(
        DB_URI,
        DB_USER,
        DB_PASSWORD,
        DB_HOST,
        DB_PORT,
        DB_NAME
    )

    class Config:
        """Configurações do pydantic, como, por exemplo, se as variáveis de ambiente são case sensitive ou não."""
        case_sensitive = True


# lru_cache() é um decorator que armazena o resultado da função
@lru_cache()
def get_settings() -> BaseSettings:
    """Retorna as configurações do projeto."""
    return Settings()


settings = get_settings()
