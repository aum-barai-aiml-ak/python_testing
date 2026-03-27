import pytest

from source import shape


@pytest.fixture
def my_rectangle():
    return shape.Rectangle(10, 20)


@pytest.fixture
def weird_rectangle():
    return shape.Rectangle(5, 6)
