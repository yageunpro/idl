import dto.error as error
from dto.request import AuthSignInRQ, AuthSignUpRQ
from dto.response import AuthSignInRO, AuthSignUpRO
from fastapi import APIRouter, responses

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


@router.get("/me", description="내 정보 가져오기")
def auth_me():
    pass


@router.get(
    "/oauth/naver",
    description="네이버 oauth request, 자동 가입 & 로그인 처리",
    response_class=responses.RedirectResponse,
)
def auth_oauth_naver():
    pass


@router.get(
    "/oauth/google",
    description="구글 oauth request, 자동 가입 & 로그인 처리",
    response_class=responses.RedirectResponse,
)
def auth_oauth_google():
    pass


@router.get(
    "/callback/naver",
    description="네이버 oauth callback",
    response_class=responses.RedirectResponse,
)
def auth_callback_naver():
    pass


@router.get(
    "/callback/google",
    description="구글 oauth callback",
    response_class=responses.RedirectResponse,
)
def auth_callback_google():
    pass
