from .appointment import router as appointment_router
from .auth import router as auth_router
from .calendar import router as calendar_router
from .user import router as user_router

__all__ = [
    "appointment_router",
    "auth_router",
    "calendar_router",
    "user_router",
]
