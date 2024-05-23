from datetime import datetime
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class Account(BaseModel):
    id: UUID = Field(description="계정 식별자")
    type: Literal["GOOGLE", "OWL"] = Field(description="계정 종류 [구글, 자체]")
    email: EmailStr = Field(description="계정 이메일")
    status: Literal["VALID", "INVALID"] = Field(description="계정 상태")


class Location(BaseModel):
    id: UUID = Field(description="장소 식별자")
    title: str = Field(description="장소 이름, from naver")
    address: str = Field(description="장소 주소, from naver")
    category: str = Field(description="장소 카테고리, from naver")
    position: list[int] = Field(description="장소 mapx, mapy")


class Participant(BaseModel):
    id: UUID = Field(description="참가자 식별자")
    name: str = Field(description="참가자 이름")


AppointmentStatus = Literal["DRAFT", "CONFIRM", "DONE", "CANCEL", "DELETE"]


class AppointmentBase(BaseModel):
    id: UUID = Field(description="약속 식별자")
    organizer_id: UUID = Field(description="약속 주최자")
    title: str = Field(description="약속 이름", examples=["약속 예제"])
    location: Location = Field(description="장소")
    status: AppointmentStatus = Field(description="약속 상태")
    confirmTime: datetime | None = Field(
        description="최종 확정된 시간, CONFIRM/DONE 상태에만 존재"
    )


class Appointment(AppointmentBase):
    description: str = Field(description="약속 설명", examples=["뭔가 엄청난 설명"])
    categoryList: list[str] = Field(
        description="카테고리", examples=[["김치", "숭실대"]]
    )
    participantList: list[Participant] = Field(description="참가자 리스트")
    deadline: datetime = Field(description="마감시간")


class Schedule(BaseModel):
    id: UUID = Field(description="일정 식별자")
    title: str = Field(description="일정 이름")
    startTime: datetime = Field(description="시작시간")
    endTime: datetime = Field(description="완료시간")
