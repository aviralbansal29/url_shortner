from fastapi import FastAPI

from app.controllers.url_generator import router as urlRouter


def addRoutes(app: FastAPI):
    app.include_router(urlRouter)
