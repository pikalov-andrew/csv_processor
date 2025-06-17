from .aggregate import AggregateCommand
from .condition import ConditionCommand
from .ordering import OrderingCommand

COMMAND_HANDLERS = {
    "where": ConditionCommand(),
    "aggregate": AggregateCommand(),
    "order_by": OrderingCommand()
}
