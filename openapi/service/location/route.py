from fastapi import APIRouter, Query

from .response import LocationRO

router = APIRouter(
    prefix="/location",
    tags=["location"],
)


@router.get("")
def location_get(q: list[str] = Query(min_length=1)) -> LocationRO:
    pass
