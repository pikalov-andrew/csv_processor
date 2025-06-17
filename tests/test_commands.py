import pytest

from src.commands import AggregateCommand
from src.commands.condition import ConditionCommand
from src.commands.ordering import OrderingCommand


@pytest.fixture
def temp_data():
    data = [
        {"name": "A", "price": "100"},
        {"name": "B", "price": "200"},
        {"name": "C", "price": "300"}
    ]
    yield data


def test_condition_filter(temp_data):
    cmd = ConditionCommand()
    filtered = cmd.handle(temp_data, "price>100")
    assert len(filtered) == 2
    filtered = cmd.handle(temp_data, "price<1000")
    assert len(filtered) == 3
    filtered = cmd.handle(temp_data, "name=B")
    assert filtered[0]["name"] == "B"
    with pytest.raises(ValueError):
        cmd.handle(temp_data, "test>100")
    with pytest.raises(ValueError):
        cmd.handle(temp_data, "name>100")
    with pytest.raises(ValueError):
        cmd.handle(temp_data, "name!=100")
    with pytest.raises(ValueError):
        cmd.handle(temp_data, "name>100>200")


def test_ordering(temp_data):
    cmd = OrderingCommand()
    sorted_data = cmd.handle(temp_data, "name=desc")
    assert [row["name"] for row in sorted_data] == ["C", "B", "A"]
    sorted_data = cmd.handle(temp_data, "name=asc")
    assert [row["name"] for row in sorted_data] == ["A", "B", "C"]
    with pytest.raises(ValueError):
        cmd.handle(temp_data, "test=desc")
    with pytest.raises(ValueError):
        cmd.handle(temp_data, "name=vverh")


def test_aggregation(temp_data):
    cmd = AggregateCommand()
    filtered = cmd.handle(temp_data, "price=max")
    assert filtered[0]["max"] == 300
    filtered = cmd.handle(temp_data, "price=min")
    assert filtered[0]["min"] == 100
    filtered = cmd.handle(temp_data, "price=avg")
    assert filtered[0]["avg"] == 200
    with pytest.raises(ValueError):
        cmd.handle(temp_data, "test=max")
    with pytest.raises(ValueError):
        cmd.handle(temp_data, "price=mean")
    with pytest.raises(ValueError):
        cmd.handle(temp_data, "pricemax")
