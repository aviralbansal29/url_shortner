from fastapi import FastAPI

from app import routes
import app.models.url as models
from configs.database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
routes.addRoutes(app)
