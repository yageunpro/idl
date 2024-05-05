from datetime import datetime

from dto.common import Schedule
from pydantic import BaseModel, Field


class AbstractSchedule(BaseModel):
    title: str = Field(description="일정 이름")
    time: datetime = Field(description="일정 시간")


ScheduleAddRO = Schedule
ScheduleInfoRO = Schedule
ScheduleListRO = list[AbstractSchedule]
