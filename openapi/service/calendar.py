import dto.error as error
from dto.request import AuthSignInRQ, AuthSignUpRQ
from dto.response import AuthSignInRO, AuthSignUpRO
from fastapi import APIRouter, responses

router = APIRouter(
    prefix="/calendar",
    tags=["calendar"],
)


@router.post("/schedule", description="수동으로 일정 추가")
def calendar_schedule_add():
    pass


@router.get("/check", description="현재 캘린더 계정 연동 상태 체크")
def calendar_check():
    pass


@router.post("/sync", description="수동으로 계정 일정 업데이트 요청")
def calendar_sync():
    pass


@router.get("/account", description="연동된 계정 리스트")
def calendar_account():
    pass


@router.post("/account", description="계정 추가 연동")
def calendar_account_add():
    pass
