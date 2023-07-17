from tortoise.models import Model
from tortoise import fields, Tortoise

from tortoise.contrib.pydantic.creator import pydantic_model_creator

from pydantic import BaseModel
from datetime import date


class Rate(Model):
    id              = fields.IntField(pk=True)
    cargo_type      = fields.CharField(max_length=255)
    value           = fields.FloatField()
    rate_aggregate: fields.ForeignKeyRelation["RateAggregator"] = fields.ForeignKeyField(
        "models.RateAggregator", related_name="rates"
    )

    class Meta:
        ordering = ["cargo_type"]

    class PydanticMeta:
        exclude = ["id"]

class RateAggregator(Model):
    id          = fields.IntField(pk=True)
    date        = fields.DateField()
    rates       = fields.ReverseRelation[Rate]

    class Meta:
        ordering = ["date"]

    class PydanticMeta:
        exclude = ["id"]

Tortoise.init_models(["src.model"], "models")


# class RateSchema(BaseModel):
#     cargo_type: str
#     value: float

# class RateAggregatorSchema(BaseModel):
#     date: date
#     rates: list[RateSchema]
#     class Config:
#         orm_mode = True
RateAggregatorSchema = pydantic_model_creator(RateAggregator, name="RatesIn")
