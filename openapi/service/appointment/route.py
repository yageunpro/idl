from datetime import datetime
from uuid import UUID

from dto.error import merge_errs
from fastapi import APIRouter
from pydantic import AnyHttpUrl

from .error import ErrAlreadyConfirmed
from .request import AppointmentAddRQ, AppointmentEditRQ
from .response import AppointmentListRO, AppointmentRO

router = APIRouter(
    prefix="/appointment",
    tags=["appointment"],
)


@router.post("", description="약속 추가")
def appointment_add(req: AppointmentAddRQ):
    pass


@router.get("/list", description="약속 list")
def appointment_list(page: int = 1, limit: int = 10) -> AppointmentListRO:
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


@router.post(
    "/{id}/join",
    description="약속 참가",
    responses={400: merge_errs(ErrAlreadyConfirmed)},
)
def appointment_join(id: UUID) -> AppointmentRO:
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
def appointment_confirm(id: UUID):
    pass
