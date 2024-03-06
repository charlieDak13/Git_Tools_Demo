import pytest
from main import collect_even_numbers


def test_collect_even_numbers():
    assert collect_even_numbers(11) == [0, 2, 4, 6, 8, 10]
    assert collect_even_numbers(0) == []
