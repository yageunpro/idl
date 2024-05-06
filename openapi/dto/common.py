from datetime import datetime
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class Account(BaseModel):
    id: UUID = Field(description="계정 식별자")
    type: Literal["NAVER", "GOOGLE", "ETC"] = Field(
        description="계정 종류 [네이버, 구글, 기타]"
    )
    email: EmailStr = Field(description="계정 이메일")
    status: Literal["VALID", "INVALID"] = Field(description="계정 상태")


class Location(BaseModel):
    title: str = Field(description="장소 이름")
    address: str = Field(description="장소 주소")
    category: str = Field(description="장소 카테고리")
    position: list[int] = Field(description="장소 mapx, mapy")


AppointmentStatus = Literal["DRAFT", "CONFIRM", "CANCEL"]


class Appointment(BaseModel):
    id: UUID = Field(description="약속 식별자")
    title: str = Field(description="약속 이름", examples=["약속 예제"])
    description: str = Field(description="약속 설명", examples=["뭔가 엄청난 설명"])
    location: Location = Field(description="장소")
    keywordList: list[str] = Field(
        description="키워드", examples=[["홈파티", "술", "고기!"]]
    )
    participantList: list[str] = Field(
        description="참가자 리스트", examples=[["홍길동", "김아무개"]]
    )
    status: AppointmentStatus = Field(description="약속 상태")
    time: datetime | None = Field(description="확정된 시간, CONFIRM 상태에만 존재")


class Schedule(BaseModel):
    id: UUID = Field(description="일정 식별자")
    title: str = Field(description="일정 이름")
    startTime: datetime = Field(description="시작시간")
    endTime: datetime = Field(description="완료시간")
