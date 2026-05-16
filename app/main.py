from fastapi import FastAPI

from app.core.settings import settings

app = FastAPI(title=settings.project_name)


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}
