import pytest
from parametrization.test_data.test_data import auth_endpoints

def id_val(val):
    return val[0]

@pytest.mark.parametrize("data", auth_endpoints)
def test_with_generator(data):
    print(data)