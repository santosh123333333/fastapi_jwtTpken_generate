from fastapi import FastAPI

from app.db.database import Base,engine
from app.model import user
from app.router import auth




app=FastAPI()


app.include_router(auth.router)


Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return{
        "message":"Welcome to fastapi"
    }
