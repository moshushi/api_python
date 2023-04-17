import pytest
import requests

# Example with single parameter
@pytest.mark.parametrize("param", [1,2,3,4])
def test_one(param):
    assert param % 2 == 0