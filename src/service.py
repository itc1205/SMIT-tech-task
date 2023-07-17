import src.helper_schemas as schemas
from src import model

from fastapi import HTTPException


async def add_new_schema(new_schema: schemas.AddNewSchema):
    for date in new_schema.__root__.keys():
        ra = await model.RateAggregator.create(date=date)
        for rate in new_schema.__root__[date]:
            await model.RateAtom.create(**rate.dict(), rate_aggregate=ra)

    return {200: "success"}


async def calculate(data: schemas.CalculateData):
    rate_aggregator = await model.RateAggregator.filter(date=data.date).first()

    if rate_aggregator is None:
        raise HTTPException(status_code=404, detail=f"Date: {data.date} is not found")

    val = (
        await model.RateAtom.filter(
            cargo_type=data.cargo_type, rate_aggregate=rate_aggregator
        )
        .first()
        .values_list("rate", flat=True)
    )

    if val is None:
        raise HTTPException(
            status_code=404, detail=f"Cargo type: {data.cargo_type} is not found"
        )
    return val * data.value
