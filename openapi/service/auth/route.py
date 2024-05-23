import dto.error as error
from fastapi import APIRouter, responses

from .request import AuthSignInRQ, AuthSignUpRQ
from .response import AuthSignInRO, AuthSignUpRO

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.get(
    "/oauth/google",
    description="구글 oauth req, ref 값으로 redirect 될 페이지 설정 가능",
    response_class=responses.RedirectResponse,
)
def auth_oauth_google(ref: str | None = None):
    pass


@router.get(
    "/callback/google",
    description="구글 oauth callback (server-side)",
    response_class=responses.RedirectResponse,  # accessToken / refreshToken Header 로 추가하기
)
def auth_callback_google():
    pass


@router.post(
    "/dev/signup",
    description="회원가입",
    responses={400: error.merge_errs(error.ErrEmailDuplicated)},
)
def auth_signup(req: AuthSignUpRQ) -> AuthSignUpRO:
    pass


@router.post(
    "/dev/signin",
    description="로그인",
    responses={401: error.merge_errs(error.ErrLoginValidation)},
)
def auth_signin(req: AuthSignInRQ) -> AuthSignInRO:
    pass
