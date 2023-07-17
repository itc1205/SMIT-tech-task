from dataclasses import dataclass
from src.domain import exceptions

from datetime import date

@dataclass(frozen=True)
class Rate:
    cargo_type: str
    value: float

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Rate):
            return __value.cargo_type == self.cargo_type
        raise NotImplementedError

    def __hash__(self) -> int:
        return hash(self.cargo_type)
    
class RateAggregate:
    rates: dict[date, set[Rate]]

    def __init__(self) -> None:
        self.rates = dict()

    def add_rate(self, date: date, rate: Rate):
        if not date in self.rates.keys():
            self.rates[date] = set()
        self.rates[date].add(rate)
    
    def get_rates(self, date: date) -> set[Rate]:
        if not date in self.rates.keys():
            raise exceptions.DateNotFound
        return self.rates[date]
    
    def calculate_rate(self, date: date, cargo_type: str, value: float):
        if not date in self.rates.keys():
            raise exceptions.DateNotFound
        for rate in self.rates[date]:
            if rate.cargo_type == cargo_type:
                return rate.value * value
        raise exceptions.RateNotFound
