#!/usr/bin/env python


from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models.task import Task
from schemas import CreateTask, UpdateTask
from sqlalchemy import select
from models.user import User
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.execute(select(Task)).scalars().all()
    return tasks


@router.get('/{task_id}/')
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.execute(select(Task).where(Task.id == task_id)).scalar_one_or_none()
    if task is None:
        raise HTTPException(status_code=404, detail='Task was not found')
    return task


@router.post('/create/')
async def create_task(task: CreateTask, user_id: int, db: Annotated[Session, Depends(get_db)]):
    try:
        existing_user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
        if existing_user is None:
            raise HTTPException(status_code=404, detail='User  was not found')

        new_task = Task(**task.model_dump(), user_id=user_id)
        db.add(new_task)
        db.commit()

        return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
    except Exception as e:
        logger.error(f'Error creating task: {e}')
        raise HTTPException(status_code=500, detail='Internal Server Error')


@router.put('/update/{task_id}')
async def update_task(task_id: int, task: UpdateTask, db: Annotated[Session, Depends(get_db)]):
    try:
        existing_task = db.query(Task).filter(Task.id == task_id).first()
        if not existing_task:
            raise HTTPException(status_code=404, detail='Task not found')

        for key, value in task.model_dump().items():
            setattr(existing_task, key, value)

        db.commit()
        db.refresh(existing_task)
        return existing_task
    except Exception as e:
        logger.error(f'Error updating task: {e}')
        raise HTTPException(status_code=500, detail='Internal Server Error')


@router.delete('/delete/{task_id}')
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    try:
        existing_task = db.query(Task).filter(Task.id == task_id).first()
        if not existing_task:
            raise HTTPException(status_code=404, detail='Task not found')

        db.delete(existing_task)
        db.commit()
        return
    except Exception as e:
        logger.error(f'Error deleting task: {e}')
        raise HTTPException(status_code=500, detail='Internal Server Error')
