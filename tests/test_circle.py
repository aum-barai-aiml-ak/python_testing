import pytest
import math

from source import shape

class TestCircle:
    
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shape.Circle(10)


    def teardown_method(self, method):
        print(f"tearing down {method}")

    def test_area(self):
        assert self.circle.area() ==  math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        assert self.circle.perimeter() == self.circle.radius * math.pi

    def test_two(self):
        assert True