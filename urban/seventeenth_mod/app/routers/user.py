#!/usr/bin/env python


from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models.user import User
from schemas import CreateUser, UpdateUser
from sqlalchemy import select
from slugify import slugify
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.execute(select(User)).scalars().all()
    return users


@router.get('/{user_id}/')
async def by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail='User  was not found')
    return user



@router.post('/create/')
async def create_user(user: CreateUser , db: Annotated[Session, Depends(get_db)]):
    try:
        user_slug = slugify(user.username)
        existing_user = db.execute(select(User).where(User.slug == user_slug)).scalar_one_or_none()
        if existing_user:
            raise HTTPException(status_code=400, detail='Slug already exists')
        new_user = User(**user.model_dump(), slug=user_slug)
        db.add(new_user)
        db.commit()

        return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful', 'user': new_user}
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put('/update/{user_id}')
async def update_user(user_id: int, user: UpdateUser , db: Annotated[Session, Depends(get_db)]):
    try:

        existing_user = db.query(User).filter(User.id == user_id).first()
        if not existing_user:
            raise HTTPException(status_code=404, detail="User  not found")


        for key, value in user.model_dump().items():
            setattr(existing_user, key, value)

        db.commit()
        db.refresh(existing_user)
        return existing_user
    except Exception as e:
        logger.error(f"Error updating user: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.delete('/delete/{user_id}')
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    try:

        existing_user = db.query(User).filter(User.id == user_id).first()
        if not existing_user:
            raise HTTPException(status_code=404, detail="User  not found")

        db.delete(existing_user)
        db.commit()
        return
    except Exception as e:
        logger.error(f"Error deleting user: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

