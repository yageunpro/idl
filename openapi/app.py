import dto.error as error
import service
from fastapi import APIRouter, Depends, FastAPI
from fastapi.openapi.models import Server
from fastapi.responses import RedirectResponse
from fastapi.security import APIKeyHeader

app = FastAPI(
    title="Owl API",
    version="0.0.1-alpha",
    servers=[
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

router = APIRouter(dependencies=[Depends(accessToken), Depends(refreshToken)])
router.include_router(service.auth_router)
router.include_router(service.appointment_router)
router.include_router(service.calendar_router)

app.include_router(router)


@app.get("/", include_in_schema=False)
def main():
    return RedirectResponse("/docs")
