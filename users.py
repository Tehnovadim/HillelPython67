import requests

limit = 208

url = f"https://dummyjson.com/users?limit={limit}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    users_aged_28 = [f"{user['firstName']} {user['lastName']}" for user in data["users"] if user["age"] == 28]

    print(f"Найдено {len(users_aged_28)} пользователей возрастом 28 лет.")

    if len(users_aged_28) >= 17:
        users_aged_28 = users_aged_28[:17]

    print("Имена всех пользователей, возраст которых 28 лет:")
    for name in users_aged_28:
        print(name)
else:
    print("Ошибка при запросе данных:", response.status_code)
