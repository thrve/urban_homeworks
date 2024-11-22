#!/usr/bin/env python


from fastapi import FastAPI

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
def user(user_id: int):
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user')
def user_info(username: str, age: int):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'


if __name__ == '__main__':
    uvicorn.run('module_16_1:app', host=ip_addr, port=8000, reload=True)
