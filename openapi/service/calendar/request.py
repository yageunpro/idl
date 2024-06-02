from datetime import datetime
from uuid import UUID

from dto.common import Location, Schedule
from pydantic import BaseModel, Field


class ScheduleAddRQ(BaseModel):
    title: str = Field(description="일정 이름")
    startTime: datetime = Field(description="시작시간")
    endTime: datetime = Field(description="완료시간")
