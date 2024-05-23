from dto.common import Appointment, AppointmentBase
from pydantic import BaseModel, Field


class AppointmentRO(Appointment):
    pass


class AbstractAppointment(AppointmentBase):
    headCount: int = Field(description="참가하는 인원 수")


class AppointmentListRO(BaseModel):
    data: list[AbstractAppointment] = Field(description="데이터")
    nextToken: str = Field(description="pagination 을 위한 token")
