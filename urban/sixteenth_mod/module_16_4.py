#!/usr/bin/env python


from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import os

ip_addr = os.environ['IP']
app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    age: int


users: List[User] = []


@app.get('/users/', response_model=List[User])
def get_users():
    return users


@app.post('/user/{username}/{age}/', response_model=User)
def create_user(
    username: str = Path(min_length=5, max_length=20, description='Enter username'),
    age: int = Path(ge=18, le=120, description='Enter age'),
):
    new_id = len(users) + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}/', response_model=User)
def update_user(
    user_id: int = Path(description='Enter user ID'),
    username: str = Path(min_length=5, max_length=20, description='Enter username'),
    age: int = Path(ge=18, le=120, description='Enter age'),
):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail='User  was not found')


@app.delete('/user/{user_id}/', response_model=User)
def delete_user(user_id: int = Path(description='Enter user ID')):
    for index, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(index)
            return deleted_user
    raise HTTPException(status_code=404, detail='User  was not found')


if __name__ == '__main__':
    uvicorn.run('module_16_4:app', host=ip_addr, port=8000, reload=True)
