from dto.common import Schedule
from pydantic import BaseModel, Field

ScheduleAddRO = Schedule
ScheduleInfoRO = Schedule


class ScheduleListRO(BaseModel):
    data: list[Schedule] = Field(description="데이터")
    nextToken: str = Field(description="pagination token")
