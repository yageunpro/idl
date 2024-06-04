from datetime import datetime
from uuid import UUID

from dto.common import AppointmentStatus
from dto.error import merge_errs
from fastapi import APIRouter
from pydantic import AnyHttpUrl

from .error import ErrAlreadyConfirmed
from .request import (
    AppointmentAddRQ,
    AppointmentConfirmRQ,
    AppointmentEditRQ,
    JoinNonmemberRQ,
)
from .response import AppointmentListRO, AppointmentRO

router = APIRouter(
    prefix="/appointment",
    tags=["appointment"],
)


@router.post("", description="약속 추가")
def appointment_add(req: AppointmentAddRQ) -> AppointmentRO:
    pass


@router.get(
    "/list",
    description="""
            약속 list\n
            [삭제 약속은 보이지 않음]\n
            정렬 순서: 미확정 / 확정 순서대로\n
            완료 기준: time (확정시간) 기준 오늘 이전 날짜[KST]\n
            [미확정]: created_at 기준 가장 최근에 만든 약속이 맨위로\n
            [확정]: time (확정시간) 기준 임박한 약속부터\n
            [완료]: time (확정시간) 기준 마지막에 수행한 약속부터\n
            """,
)
def appointment_list(
    type: AppointmentStatus,
    page_token: str | None = None,
    limit: int | None = 10,
) -> AppointmentListRO:
    pass


@router.get("/{id}", description="약속 세부 정보 가져오기")
def appointment_info(id: UUID) -> AppointmentRO:
    pass


@router.patch(
    "/{id}",
    description="약속 수정 (키워드, 장소 등..)",
    responses={400: merge_errs(ErrAlreadyConfirmed)},
)
def appointment_edit(id: UUID, req: AppointmentEditRQ) -> AppointmentRO:
    pass


@router.get("/{id}/share", description="약속 공유 URL 가져오기")
def appointment_share_url(id: UUID) -> AnyHttpUrl:
    pass


@router.delete("/{id}", description="약속 삭제")
def appointment_delete(id: UUID):
    pass


@router.post(
    "/{id}/join",
    description="약속 참가",
    responses={400: merge_errs(ErrAlreadyConfirmed)},
)
def appointment_join(id: UUID) -> AppointmentRO:
    pass


@router.post(
    "/{id}/join/nonmember",
    description="약속 참가",
    responses={400: merge_errs(ErrAlreadyConfirmed)},
)
def appointment_join_nonmember(id: UUID, req: JoinNonmemberRQ) -> AppointmentRO:
    pass


@router.get(
    "/{id}/recommend",
    description="약속 추천 시간 가져오기",
    responses={400: merge_errs(ErrAlreadyConfirmed)},
)
def appointment_get_recommend(id: UUID) -> list[datetime]:
    pass


@router.post(
    "/{id}/confirm",
    description="약속 확정",
    responses={400: merge_errs(ErrAlreadyConfirmed)},
)
def appointment_confirm(id: UUID, req: AppointmentConfirmRQ):
    pass
