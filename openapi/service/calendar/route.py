from datetime import datetime, timedelta
from uuid import UUID

from fastapi import APIRouter

from .request import ScheduleAddRQ
from .response import ScheduleAddRO, ScheduleInfoRO, ScheduleListRO

router = APIRouter(
    prefix="/calendar",
    tags=["calendar"],
)


@router.post("/schedule", description="일정 추가")
def calendar_schedule_add(req: ScheduleAddRQ) -> ScheduleAddRO:
    pass


@router.get("/schedule/{id}", description="일정 세부 정보")
def calendar_schedule_info(id: UUID) -> ScheduleInfoRO:
    pass


@router.delete("/schedule/{id}", description="일정 삭제")
def calendar_schedule_delete(id: UUID):
    pass


@router.get("/schedule/list", description="전체 일정 리스트")
def calendar_schedule_list(
    start: datetime = datetime.now(),
    end: datetime = datetime.now() + timedelta(days=365),
    page_token: str | None = None,
    limit: int | None = 10,
) -> ScheduleListRO:
    pass


@router.post("/sync", description="수동으로 연동 계정 업데이트 요청")
def calendar_sync():
    pass
