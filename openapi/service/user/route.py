from typing import Literal
from uuid import UUID

from fastapi import APIRouter

from .response import UserAccountRO, UserMeRO

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.get(
    "/me",
    description="내 정보 가져오기",
)
def user_me() -> UserMeRO:
    pass


@router.get(
    "/account",
    description="연동된 계정 가져오기",
)
def user_account() -> UserAccountRO:
    pass


@router.post(
    "/account",
    description="계정 추가 연동",
)
def user_add_account(type: Literal["google"]):
    pass


@router.post("/account/{id}", description="계정 재인증")
def user_verify_account(id: UUID):
    pass


@router.delete("/account/{id}", description="계정 연동 해제")
def user_delete_account(id: UUID):
    pass
