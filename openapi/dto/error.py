from typing import Type

from pydantic import BaseModel, Field


class BaseError(BaseModel):
    _description: str = "description of error"
    errorId: str = Field(description="Error Id", examples=["ErrSampleId"])
    message: None | str = Field(
        description="Extra Message", examples=["Detail information"]
    )


class ErrValidationFail(BaseError):
    """
    http code 422
    """

    _description = "When validation fail"
    errorId: str = Field(examples=["ErrValidationFail"])


class ErrAuthFail(BaseError):
    """
    http code 401
    """

    _description = "When forbidden actions is requested"
    errorId: str = Field(examples=["ErrDenied"])


class ErrUnexpected(BaseError):
    """
    http code 500
    """

    _description = "When unexpected error not handled"
    errorId: str = Field(examples=["ErrUnexpected"])


class ErrEmailDuplicated(BaseError):
    _description = "When email is duplicated"
    errorId: str = Field(examples=["ErrEmailDuplicate"])


class ErrLoginValidation(BaseError):
    _description = "When login information is not valid"
    errorId: str = Field(examples=["ErrLoginValidation"])


def merge_errs(*errs: Type[BaseError]):
    return {
        "description": "Multiple Errors",
        "content": {
            "application/json": {
                "examples": {
                    err.__name__: {
                        "summary": err.__name__,
                        "description": str(err._description),
                        "value": {
                            "errorId": err.__name__,
                            "message": "Detail information",
                        },
                    }
                    for err in errs
                }
            }
        },
    }
