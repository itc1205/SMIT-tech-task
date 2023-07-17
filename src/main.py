from typing import List
from fastapi import FastAPI

from src.helper_schemas import CalculateData, AddNewSchema

from src.config import tortoise_cfg
from src import service

from tortoise.contrib.fastapi import register_tortoise, HTTPNotFoundError

api = FastAPI()


@api.post("/", responses={404: {"model": HTTPNotFoundError}})
async def post_schema(new_schema: AddNewSchema):
    return await service.add_new_schema(new_schema)


@api.post("/calc", responses={404: {"model": HTTPNotFoundError}})
async def calculate(data: CalculateData):
    return await service.calculate(data)


register_tortoise(
    api,
    # db_url="sqlite://:memory:",
    config=tortoise_cfg,
    modules={"models": ["src.model"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
