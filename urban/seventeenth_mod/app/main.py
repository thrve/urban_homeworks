#!/usr/bin/env python


from fastapi import FastAPI

from routers.tasks import router as tasks_router
from routers.user import router as user_router
from backend.db import Base, engine

import uvicorn
import os

app = FastAPI()
Base.metadata.create_all(bind=engine)

ip_addr = os.environ['IP']


@app.get('/')
def welcome():
    return {'message': 'Welcome to Taskmanager'}


app.include_router(tasks_router)
app.include_router(user_router)


if __name__ == '__main__':
    uvicorn.run('main:app', host=ip_addr, port=8000, reload=True)
