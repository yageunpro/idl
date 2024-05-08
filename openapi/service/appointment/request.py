from datetime import datetime

from dto.common import Location, Schedule
from pydantic import BaseModel, Field


class AppointmentAddRQ(BaseModel):
    title: str = Field(description="약속 이름", examples=["약속 예제"])
    description: str = Field(description="약속 설명", examples=["뭔가 엄청난 설명"])
    location: Location | None = Field(description="장소")
    keywordList: list[str] = Field(
        description="키워드", examples=[["홈파티", "술", "고기!"]]
    )
    startTime: datetime | None = Field(description="시작시간")
    endTime: datetime = Field(description="끝나는 시간")


class AppointmentEditRQ(BaseModel):
    title: str | None = Field(description="약속 이름", examples=["약속 제목 수정"])
    description: str | None = Field(description="약속 설명", examples=["설명 수정"])
    location: Location | None = Field(description="장소")
    keywordList: list[str] | None = Field(
        description="키워드", examples=[["키워드", "수정", "전체보내기"]]
    )


class AppointmentJoinNonmember(BaseModel):
    username: str = Field(description="이름")
    scheduleList: list[Schedule] = Field(description="일정 리스트")


class AppointmentConfirm(BaseModel):
    time: datetime = Field(description="확정날짜")
