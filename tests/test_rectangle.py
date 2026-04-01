import pytest

from source.shape import Rectangle


def test_area(my_rectangle: Rectangle):

    assert my_rectangle.area() == 10 * 20


def test_perimeter(my_rectangle: Rectangle):
    assert my_rectangle.perimeter() == (10 * 2) + (20 * 2)


def test_not_equal(my_rectangle: Rectangle, weird_rectangle: Rectangle):
    assert my_rectangle == weird_rectangle


def test_fail():
    pytest.fail(
        "deliberately failing for demo purpose, Lorem ipsum dolor sit amet, "
        "consectetur adipiscing elit. Cras facilisis, massa in suscipit "
        "dignissim, mauris lacus molestie nisi, quis varius metus nulla ut ipsum."
    )
