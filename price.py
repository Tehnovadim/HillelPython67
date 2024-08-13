def calculate_discounted_price(price: float, discount: float) -> float:
    if price < 0:
        raise ValueError("Цена не может быть меньше 0.")
    if discount < 0 or discount > 100:
        raise ValueError("Скидка должна быть в пределах от 0 до 100.")
    
    discounted_price = price * (1 - discount / 100)
    return round(discounted_price, 2)
