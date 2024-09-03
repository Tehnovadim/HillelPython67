def generate_greeting(username):
    return f"<h1>Вітаємо тебе, шановний {username}</h1>"

username = "Олександр"
html_greeting = generate_greeting(username)
print(html_greeting)