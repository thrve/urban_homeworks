#!/usr/bin/env python


from fastapi import FastAPI, Path
from typing import Annotated

import uvicorn
import os


ip_addr = os.environ['IP']


app = FastAPI()


@app.get('/')
def hello_index():
    return {
        'message': 'Hello!',
    }


@app.get('/user/admin')
def admin():
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
def user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]):
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user')
def user_info(
    username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
    age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')],
):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'


if __name__ == '__main__':
    uvicorn.run('module_16_1:app', host=ip_addr, port=8000, reload=True)
