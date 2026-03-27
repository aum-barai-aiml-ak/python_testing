import time

import pytest

import source.my_functions as my_functions


def test_add():
    result = my_functions.add(1, 4)
    assert result == 5


def test_add_strings():
    result = my_functions.add("i like ", "pizza")
    assert result == "i like pizza"


def test_divide():
    result = my_functions.divide(10, 5)
    assert result == 2


def test_divdie_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(10, 0)


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(10, 5)
    assert result == 2


# @pytest.mark.skip(reason="this feature is currently broken")
# def test_add():
#     assert my_functions.add(1, 2) == 3


@pytest.mark.xfail(reason="we know we can't divide by zero")
def test_divide_zero_droken():
    my_functions.divide(10, 0)
