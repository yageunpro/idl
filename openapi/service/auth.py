import dto.error as error
from dto.request import AuthSignInRQ, AuthSignUpRQ
from dto.response import AuthSignInRO, AuthSignUpRO
from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post(
    "/signup",
    description="회원가입",
    responses={400: error.merge_errs(error.ErrEmailDuplicated)},
)
def auth_signup(req: AuthSignUpRQ) -> AuthSignUpRO:
    pass


@router.post(
    "/signin",
    description="로그인",
    responses={401: error.merge_errs(error.ErrLoginValidation)},
)
def auth_signin(req: AuthSignInRQ) -> AuthSignInRO:
    pass
