#!/usr/bin/env python


__all__ = ('router',)

from aiogram import Router
from .calories_survey import router as calories_survey_router
from .registration_survey import router as registration_router
from .buying_survey import router as buying_router
from .calories_calculator import router as calculator


router = Router(name=__name__)

router.include_routers(
    calories_survey_router,
    registration_router,
    buying_router,
    calculator,
)
