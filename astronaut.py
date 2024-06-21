import requests

data = {
    "people": [
        {"craft": "ISS", "name": "Oleg Kononenko"},
        {"craft": "ISS", "name": "Nikolai Chub"},
        {"craft": "ISS", "name": "Tracy Caldwell Dyson"},
        {"craft": "ISS", "name": "Matthew Dominick"},
        {"craft": "ISS", "name": "Michael Barratt"},
        {"craft": "ISS", "name": "Jeanette Epps"},
        {"craft": "ISS", "name": "Alexander Grebenkin"},
        {"craft": "ISS", "name": "Butch Wilmore"},
        {"craft": "ISS", "name": "Sunita Williams"},
        {"craft": "Tiangong", "name": "Li Guangsu"},
        {"craft": "Tiangong", "name": "Li Cong"},
        {"craft": "Tiangong", "name": "Ye Guangfu"}
    ],
    "number": 12,
    "message": "success"
}

for astronaut in data['people']:
    print(astronaut['name'])
