from typing import List
from fastapi import FastAPI

from src.helper_schemas import CalculateData, OurSchema

from src.config import tortoise_cfg
from src import service

from tortoise.contrib.fastapi import register_tortoise, HTTPNotFoundError

api = FastAPI()


@api.post("/")
async def set_schema(new_schema: OurSchema):
    """Clears and sets new schema"""
    return await service.set_new_schema(new_schema)

@api.put("/")
async def set_schema(new_schema: OurSchema):
    """Appends existing schema"""
    return await service.append_schema(new_schema)


@api.post("/calc", responses={404: {"model": HTTPNotFoundError}})
async def calculate(data: CalculateData):
    """Finds and calculates rate"""
    return await service.calculate(data)


register_tortoise(
    api,
    # db_url="sqlite://:memory:",
    config=tortoise_cfg,
    modules={"models": ["src.model"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
