import pytest

def calculate_discounted_price(price: float, discount: float) -> float:
    if price < 0:
        raise ValueError("Цена не может быть меньше 0.")
    if discount < 0 or discount > 100:
        raise ValueError("Скидка должна быть в пределах от 0 до 100.")
    
    discounted_price = price * (1 - discount / 100)
    return round(discounted_price, 2)

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
