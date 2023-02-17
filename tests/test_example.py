import pytest

from src.summator import summator


@pytest.mark.smoke
def test_one():
    assert summator(10, 20) == 30


@pytest.mark.skip
def test_two():
    assert summator(-10, -4) == 30
