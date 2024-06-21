import requests

url = "https://dummyjson.com/users"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    users_aged_28 = [f"{user['firstName']} {user['lastName']}" for user in data["users"] if user["age"] == 28]
    print("Имена всех пользователей, возраст которых 28 лет:")
    for name in users_aged_28:
        print(name)
else:
    print("Ошибка при запросе данных:", response.status_code)
