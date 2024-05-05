from uuid import UUID

from dto.common import Account
from pydantic import BaseModel, EmailStr, Field


class UserMeRO(BaseModel):
    id: UUID = Field(description="유저 식별자")
    username: str = Field(description="이름")
    email: EmailStr = Field(description="계정 대표 이메일 (가입시 이메일)")


class UserAccountRO(BaseModel):
    accountList: list[Account] = Field(description="연동된 계정")
