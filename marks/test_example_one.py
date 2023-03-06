"""Пример маркировки проваленных тестов"""
import pytest


@pytest.mark.regress
@pytest.mark.skip(reason="Mantis-337")
def test_example_one():
    """Тест который всегда проваливается"""
    assert 0


@pytest.mark.regress
@pytest.mark.xfail(strict=True)
def test_example_two():
    """Тест который всегда проваливается"""
    assert False
