import dto.error as error
import service
import service.location
from fastapi import APIRouter, Depends, FastAPI
from fastapi.openapi.models import Server
from fastapi.responses import RedirectResponse
from fastapi.security import APIKeyHeader

app = FastAPI(
    title="Owl API",
    version="0.1.0",
    servers=[
        Server(url="https://yageun.pro", description="prod server").model_dump(),
        Server(url="http://127.0.0.1:8000", description="dev server").model_dump(),
    ],
    responses={
        401: {"description": "Authentication Error", "model": error.ErrAuthFail},
        422: {"description": "Validation Error", "model": error.ErrValidationFail},
        500: {"description": "Unexpected Error", "model": error.ErrUnexpected},
    },
)

accessToken = APIKeyHeader(name="access_token", scheme_name="AccessToken")
refreshToken = APIKeyHeader(name="refresh_token", scheme_name="RefreshToken")


secure_router = APIRouter(
    prefix="/api", dependencies=[Depends(accessToken), Depends(refreshToken)]
)
secure_router.include_router(service.auth.router)
secure_router.include_router(service.appointment.router)
secure_router.include_router(service.calendar.router)
secure_router.include_router(service.location.router)
secure_router.include_router(service.user.router)

app.include_router(secure_router)


@app.get("/", include_in_schema=False)
def main():
    return RedirectResponse("/docs")
