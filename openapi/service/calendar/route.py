import dto.error as error
from fastapi import APIRouter, responses

from .response import ScheduleAddRO, ScheduleInfoRO, ScheduleListRO

router = APIRouter(
    prefix="/calendar",
    tags=["calendar"],
)


@router.post("/schedule", description="일정 추가")
def calendar_schedule_add() -> ScheduleAddRO:
    pass


@router.get("/schedule/{id}", description="일정 세부 정보")
def calendar_schedule_info() -> ScheduleInfoRO:
    pass


@router.delete("/schedule/{id}", description="일정 삭제")
def calendar_schedule_delete():
    pass


@router.get("/schedule/list", description="전체 일정 리스트")
def calendar_schedule_list(page: int = 1, limit: int = 10) -> ScheduleListRO:
    pass


@router.post("/sync", description="수동으로 연동 계정 업데이트 요청")
def calendar_sync():
    pass
