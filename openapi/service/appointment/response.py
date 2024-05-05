from datetime import datetime
from typing import Literal

from dto.common import Appointment
from pydantic import BaseModel, Field


class AppointmentRO(Appointment):
    pass


class AbstractAppointment(BaseModel):
    title: str = Field(description="약속 이름")
    locaction: str = Field(description="간략한 장소 정보")
    headcount: int = Field(description="참가하는 인원 수")
    status: Literal["PROGRESS", "CONFIRM"] = Field(description="약속 상태")
    time: datetime | None = Field(description="확정 시간, 확정시에만 나옴")


AppointmentListRO = list[AbstractAppointment]
