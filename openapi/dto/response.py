from typing import Literal
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class AuthSignUpRO(BaseModel):
    access_token: str = Field(description="access token")
    refresh_token: str = Field(description="refresh token")


class AuthSignInRO(BaseModel):
    access_token: str = Field(description="user")
    refresh_token: str = Field(description="user")


class UserMeRO(BaseModel):
    id: UUID = Field(description="유저 식별자")
    username: str = Field(description="이름")
    email: EmailStr = Field(description="계정 대표 이메일 (가입시 이메일)")


class UserAccountRO(BaseModel):
    class Account(BaseModel):
        id: UUID = Field(description="계정 식별자")
        type: Literal["NAVER", "GOOGLE", "ETC"] = Field(
            description="계정 종류 [네이버, 구글, 기타]"
        )
        email: EmailStr = Field(description="계정 이메일")
        status: Literal["VALID", "INVALID"] = Field(description="계정 상태")

    accountList: list[Account] = Field(description="연동된 계정")
