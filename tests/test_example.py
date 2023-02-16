from src.summator import summator
# import src.summator


def test_one():
    assert summator(10, 20) == 30


def test_two():
    # summator(-10, -4) == -14
    assert summator(-10, -4) == 30
