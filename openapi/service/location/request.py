from datetime import datetime
from uuid import UUID

from dto.common import Location, Schedule
from pydantic import BaseModel, Field


class AppointmentAddRQ(BaseModel):
    title: str = Field(description="약속 이름", examples=["약속 예제"])
    description: str = Field(description="약속 설명", examples=["뭔가 엄청난 설명"])
    location_id: UUID | None = Field(description="장소")
    categoryList: list[str] = Field(
        description="카테고리", examples=[["김치", "숭실대"]]
    )
    deadline: datetime = Field(description="마감시간")


class AppointmentEditRQ(BaseModel):
    title: str | None = Field(description="약속 이름", examples=["약속 제목 수정"])
    description: str | None = Field(description="약속 설명", examples=["설명 수정"])
    location_id: UUID | None = Field(description="장소")
    categoryList: list[str] = Field(
        description="카테고리", examples=[["김치", "숭실대"]]
    )


class JoinNonmemberRQ(BaseModel):
    username: str = Field(description="이름")
    scheduleList: list[Schedule] = Field(description="일정 리스트")


class AppointmentConfirmRQ(BaseModel):
    time: datetime = Field(description="확정날짜")
