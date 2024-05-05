from dto.error import BaseError
from pydantic import Field


class ErrAlreadyConfirmed(BaseError):
    """
    이미 완료된 약속
    """

    _description = "When appointment already confirmed"
    errorId: str = Field(examples=["ErrAppointmentConfirmed"])
