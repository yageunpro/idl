import dto.error as error
from fastapi import APIRouter, responses

from .request import AuthSignInRQ, AuthSignUpRQ
from .response import AuthSignInRO, AuthSignUpRO

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


@router.get(
    "/oauth/naver",
    description="네이버 oauth request, 자동 가입 & 로그인 처리",
    response_class=responses.RedirectResponse,
)
def auth_oauth_naver(ref: str | None = None):
    pass


@router.get(
    "/oauth/google",
    description="구글 oauth request, 자동 가입 & 로그인 처리",
    response_class=responses.RedirectResponse,
)
def auth_oauth_google(ref: str | None = None):
    pass


@router.get(
    "/callback/naver",
    description="네이버 oauth callback (server-side)",
    response_class=responses.RedirectResponse,
)
def auth_callback_naver(
    code: str,
    state: str,
    error: str | None = None,
    error_description: str | None = None,
):
    # https://developers.naver.com/docs/login/devguide/devguide.md#3-4-3-%EB%84%A4%EC%9D%B4%EB%B2%84-%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EC%97%B0%EB%8F%99-%EA%B2%B0%EA%B3%BC-callback-%EC%A0%95%EB%B3%B4
    pass


@router.get(
    "/callback/google",
    description="구글 oauth callback (server-side)",
    response_class=responses.RedirectResponse,
)
def auth_callback_google():
    pass
