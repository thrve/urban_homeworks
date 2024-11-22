#!/usr/bin/env python


from fastapi import FastAPI, Path
from typing import Dict, Annotated

import uvicorn
import os


ip_addr = os.environ['IP']
app = FastAPI()


users: Dict[str, str] = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users/')
def get_users():
    return users


@app.post('/user/{username}/{age}/')
def create_user(
    username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', examples=['UrbanUser'])],
    age: Annotated[int, Path(ge=18, le=120, description='Enter age', examples=['24'])],
):
    new_id = str(len(users) + 1)
    users[new_id] = f'Имя: {username}, возраст: {age}'
    return f'User {new_id} is registered'


@app.put('/user/{user_id}/{username}/{age}/')
def update_user(
    user_id: Annotated[str, Path(description='Enter user ID', examples=['1'])],
    username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', examples=['UrbanProfi'])],
    age: Annotated[int, Path(ge=18, le=120, description='Enter age', examples=['28'])],
):
    if user_id in users:
        users[user_id] = f'Имя: {username}, возраст: {age}'
        return f'User {user_id} has been updated'
    else:
        return f'User {user_id} not found'


@app.delete('/user/{user_id}/')
def delete_user(user_id: Annotated[str, Path(description='Enter user ID', examples=['2'])]):
    if user_id in users:
        del users[user_id]
        return f'User {user_id} has been deleted'
    else:
        return f'User {user_id} not found'


if __name__ == '__main__':
    uvicorn.run('module_16_3:app', host=ip_addr, port=8000, reload=True)
