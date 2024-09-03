from typing import Callable

def result_as_dict_decorator(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return {'result': result}
    return wrapper

@result_as_dict_decorator
def add_two_numbers(number_one: int, number_two: int) -> int:
    return number_one + number_two

print(add_two_numbers(2, 7))  # Виведе: {'result': 9}

@result_as_dict_decorator
def divide_two_numbers(number_one: int, number_two: int) -> float:
    return number_one / number_two

print(divide_two_numbers(10, 2))  # Виведе: {'result': 5.0}
