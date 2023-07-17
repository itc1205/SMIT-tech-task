from tortoise.models import Model
from tortoise import fields, Tortoise

from tortoise.contrib.pydantic.creator import pydantic_model_creator


class RateAtom(Model):
    id = fields.IntField(pk=True)
    cargo_type = fields.CharField(max_length=255)
    rate = fields.FloatField()
    rate_aggregate: fields.ForeignKeyRelation[
        "RateAggregator"
    ] = fields.ForeignKeyField("models.RateAggregator", related_name="rates")

    class Meta:
        ordering = ["cargo_type"]

    class PydanticMeta:
        exclude = ["id", "rate_aggregate", "rate_aggregate_id"]


class RateAggregator(Model):
    id = fields.IntField(pk=True)
    date = fields.DateField(unique=True)
    rates = fields.ReverseRelation[RateAtom]

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

RateSchema = pydantic_model_creator(RateAtom, name="Rate")
RateAggregatorSchema = pydantic_model_creator(RateAggregator, name="RatesIn")
