import pytest
from price import calculate_discounted_price

class TestCalculateDiscountedPrice:

    def test_valid_discount(self):
        assert calculate_discounted_price(100, 20) == 80.00

    def test_zero_discount(self):
        assert calculate_discounted_price(100, 0) == 100.00

    def test_max_discount(self):
        assert calculate_discounted_price(100, 100) == 0.00

    def test_negative_price(self):
        with pytest.raises(ValueError):
            calculate_discounted_price(-100, 20)

    def test_discount_more_than_100(self):
        with pytest.raises(ValueError):
            calculate_discounted_price(100, 110)

    def test_negative_discount(self):
        with pytest.raises(ValueError):
            calculate_discounted_price(100, -10)
