"""Тестирование параметризации"""

import pytest


# Example with single parameter
@pytest.mark.parametrize("param", [1, 2, 3, 4])
def test_one(param):
    assert param % 2 == 0


# Example with several parameter
@pytest.mark.parametrize("param1, param2", [
    (1, 2),
    (3, 4),
    (5, 6),
    (7, 8)
])
def test_two(param1, param2):
    assert (param1 + param2) % 3 == 0


# Example with nested parametrization
@pytest.mark.parametrize("param2", [1, 2, 3, 4, 5])
@pytest.mark.parametrize("param1", [6, 7, 8, 9, 0])
def test_three_nested(param1, param2):
    assert (param1 + param2) % 2 == 0
