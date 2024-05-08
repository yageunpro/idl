from datetime import datetime
from uuid import UUID

from dto.common import Appointment, AppointmentStatus
from pydantic import BaseModel, Field


class AppointmentRO(Appointment):
    pass


class AbstractAppointment(BaseModel):
    id: UUID = Field(description="약속 식별자")
    title: str = Field(description="약속 이름")
    locaction: str = Field(description="간략한 장소 정보")
    headcount: int = Field(description="참가하는 인원 수")
    status: AppointmentStatus = Field(description="약속 상태")
    confirmTime: datetime | None = Field(
        description="최종 확정된 시간, CONFIRM 상태에만 존재"
    )


AppointmentListRO = list[AbstractAppointment]
