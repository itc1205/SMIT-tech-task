import pytest

from datetime import date
from src import model

async def test_creating_model():
    new_model = model.Rate(
        date=date.today(),
        cargo_type="Glass",
        value=0.3
    )
    await new_model.save()
    
