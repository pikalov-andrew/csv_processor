import sys

import pytest

from cli import parse_commands


def test_cli_args():
    sys.argv = ["main.py", "-f", "products.csv", "-w", "brand=apple"]
    args = parse_commands()
    assert args["file_path"] == "products.csv"
    assert args["commands"]["where"] == "brand=apple"
    sys.argv = ["main.py", "-f", "products.csv", "-a", "price=min"]
    args = parse_commands()
    assert args["commands"]["aggregate"] == "price=min"
    sys.argv = ["main.py", "-f", "products.csv", "-o", "price=desc"]
    args = parse_commands()
    assert args["commands"]["order_by"] == "price=desc"
    sys.argv = ["main.py", "-f", "products.csv", "-a", "price=min", "-o", "name=asc"]
    with pytest.raises(SystemExit):
        parse_commands()
