import pytest
from allpairspy import AllPairs

class TestParameterized(object):

    @pytest.mark.parametrize(("brand, proc, operating system"), [
        value_list for value_list in AllPairs([
            ["DELL", "ACER"],
            ["AMD", "INTEL"],
            ["Win10", "Linux"]
        ])
    ])
    def test_with_pw(self, brand, proc, operating_system):
        assert False


    @pytest.mark.parametrize("brand", ["DELL", "ACER"])
    @pytest.mark.parametrize("proc", ["AMD", "INTEL"])
    @pytest.mark.parametrize("operating_system", ["Win10", "Linux"])
    def test_no_pw(self, brand, proc, operating_system):
        assert False