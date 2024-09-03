def print_header_footer():
    print("~" * 50)

print_header_footer()

dish_name = input("Введіть назву страви, рецепт якої вам подобається: ").strip()
recipe = input("Введіть рецепт зазначеної страви: ").strip()

formatted_dish_name = f"{'*' * 10} {dish_name.upper().replace(' ', '')} {'*' * 10}"
print(formatted_dish_name)

formatted_recipe = recipe.lower().replace(' ', '') + " 😊"
print(formatted_recipe)

meat_count = recipe.lower().count("мясо")
print(f"Кількість слів 'мясо' в рецепті: {meat_count}")

print_header_footer()
