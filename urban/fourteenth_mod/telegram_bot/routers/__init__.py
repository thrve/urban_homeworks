#!/usr/bin/env python


__all__ = ('router',)


from aiogram import Router

from .commands import router as commands_router
from .users import router as users_router


router = Router(name=__name__)

router.include_routers(
    commands_router,
    users_router,
)
