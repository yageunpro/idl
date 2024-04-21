from uuid import UUID

from dto.response import AuthSignUpRO
from fastapi import APIRouter

router = APIRouter(
    prefix="/appointment",
    tags=["appointment"],
)


@router.get("/{appointment_id}", description="약속 세부 정보 가져오기")
def appointment_get(appointment_id: UUID):
    pass


@router.patch("/{appointment_id}", description="약속 수정 (카테고리, 장소 등..)")
def appointment_patch(appointment_id: UUID):
    pass


@router.get("/{appointment_id}/share", description="약속 공유 가능한 정보 가져오기")
def appointment_share(appointment_id: UUID):
    pass


@router.post("/{appointment_id}/join", description="약속 참가")
def appointment_join(appointment_id: UUID):
    pass


@router.get("/{appointment_id}/recommend", description="약속 추천 시간 가져오기")
def appointment_get_recommend(appointment_id: UUID):
    pass


@router.post("/{appointment_id}/confirm", description="약속 확정")
def appointment_confirm(appointment_id: UUID):
    pass


@router.post("", description="약속 추가")
def appointment_add():
    pass


@router.get("/list", description="약속 list")
def appointment_list(page: int = 1, limit: int = 10) -> AuthSignUpRO:
    pass
