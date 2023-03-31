import logging

from fastapi import FastAPI

from app.api.v1.api import api_router
from config.settings import settings

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

app = FastAPI(title=settings.PROJECT_NAME,
              description=settings.PROJECT_DESCRIPTION,
              version=settings.APP_VERSION)

app.include_router(api_router, prefix=settings.API_V1_PREFIX)

if __name__ == "__main__":
    import uvicorn

    logging.info("Iniciando servidor...")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
