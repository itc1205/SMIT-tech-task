from typing import List

from fastapi import FastAPI, HTTPException
from src.model import Rate, RateAggregator, RateAggregatorSchema
from pydantic import BaseModel
from src.config import tortoise_cfg
from datetime import date

from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

api = FastAPI()


class Status(BaseModel):
    message: str

class CalculateData(BaseModel):
    value: float
    cargo_type: str
    date: date

@api.get("/", response_model=List[RateAggregatorSchema])
async def get_schema():
    
    return await RateAggregatorSchema.from_queryset(RateAggregator.all())

@api.post("/")
async def post_schema(
    new_schema: List[RateAggregatorSchema]
):
    for rate_aggregator in new_schema:    
        ra = await RateAggregator.create(date=rate_aggregator.date)
        for rate in rate_aggregator.rates:
            await Rate.create(**rate.dict(), rate_aggregate=ra)

            

@api.post("/calc")
async def calculate(data: CalculateData):
    rate_aggregator = await RateAggregator.filter(date=data.date).first()
    val = await Rate.filter(cargo_type=data.cargo_type, rate_aggregate=rate_aggregator).first().values_list("value", flat=True)
    return val * data.value


register_tortoise(
    api,
    db_url="sqlite://:memory:",
    #config=tortoise_cfg,
    modules={"models": ["src.model"]},
    generate_schemas=True,
    add_exception_handlers=True,
)



