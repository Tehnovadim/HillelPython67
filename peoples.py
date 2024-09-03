num_people = 4

ticket_price_per_person = 500
total_ticket_price = num_people * ticket_price_per_person

taxi_to_park = 600
taxi_from_park = taxi_to_park * 1.20

pizza_price_per_unit = 250
number_of_pizzas = 2
total_pizza_price = pizza_price_per_unit * number_of_pizzas
discount = 0.15
total_pizza_price_with_discount = total_pizza_price * (1 - discount)

air_hockey_price_per_game = 80
number_of_games = 8
total_air_hockey_price = air_hockey_price_per_game * number_of_games

total_expense = (total_ticket_price + taxi_to_park + taxi_from_park +
                 total_pizza_price_with_discount + total_air_hockey_price)

expense_per_person = total_expense / num_people

print(f"Кожен із вас повинен заплатити: {expense_per_person:.2f} грн")