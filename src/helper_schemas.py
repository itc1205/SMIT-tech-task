from typing import List

from pydantic import BaseModel, Field
from datetime import date

from src.model import RateSchema


class CalculateData(BaseModel):
    value: float
    cargo_type: str
    date: date


class AddNewSchema(BaseModel):
    __root__: dict[date, List[RateSchema]] = Field(
        example={"2022-01-01": [{"cargo_type": "Glass", "rate": 0.015}]}
    )
