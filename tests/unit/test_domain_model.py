import pytest

from datetime import date

from src.domain import model, exceptions


def test_aggregator_can_hold_rate():
    rate = model.Rate("Glass", 1.0)
    rate_aggregator = model.RateAggregate()

    rate_aggregator.add_rate(date=date.today(), rate=rate)

    saved_rate = rate_aggregator.get_rates(date=date.today()).pop()

    assert rate.cargo_type == saved_rate.cargo_type
    assert rate.value == saved_rate.value
