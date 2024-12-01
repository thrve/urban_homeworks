from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Annotated, List
from annotated_types import MinLen, MaxLen
import uvicorn
import os

ip_addr = os.environ['IP']
app = FastAPI()

templates = Jinja2Templates(directory='templates')


class User(BaseModel):
    id: Annotated[int, Path(description='User  ID')]
    username: Annotated[str, MinLen(5), MaxLen(20), Path(description='Введите имя пользователя')]
    age: Annotated[int, Path(ge=18, le=120, description='Введите возраст')]


users: List[User] = []


users.append(User(id=1, username='UrbanUser ', age=24))
users.append(User(id=2, username='UrbanTest', age=22))
users.append(User(id=3, username='Capybara', age=60))


@app.get('/', response_class=HTMLResponse)
def read_root(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get('/user/{user_id}/', response_class=HTMLResponse)
def get_user(request: Request, user_id: int) -> HTMLResponse:
    for existing_user in users:
        if existing_user.id == user_id:
            return templates.TemplateResponse('users.html', {'request': request, 'user': existing_user})
    raise HTTPException(status_code=404, detail='Пользователь не найден')


@app.post('/user/', response_model=User)
def create_user(user: User) -> User:
    max_id = max((existing_user.id for existing_user in users), default=0)
    new_id = max_id + 1
    new_user = User(id=new_id, **user.model_dump())
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/', response_model=User)
def update_user(user_id: int, user: User) -> User:
    for existing_user in users:
        if existing_user.id == user_id:
            existing_user.username = user.username
            existing_user.age = user.age
            return existing_user
    raise HTTPException(status_code=404, detail='Пользователь не найден')


@app.delete('/user/{user_id}/', response_model=User)
def delete_user(user_id: int) -> User:
    for index, existing_user in enumerate(users):
        if existing_user.id == user_id:
            deleted_user = users.pop(index)
            return deleted_user
    raise HTTPException(status_code=404, detail='Пользователь не найден')


if __name__ == '__main__':
    uvicorn.run('module_16_5:app', host=ip_addr, port=8000, reload=True)
