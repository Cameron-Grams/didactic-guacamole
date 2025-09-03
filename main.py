from fastapi import FastAPI
from database import Base, engine
import models
import posts

app = FastAPI()
app.include_router(posts.router)

models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
