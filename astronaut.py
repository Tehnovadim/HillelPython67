import requests
import time


def fetch_astronauts():
    try:
        response = requests.get("http://api.open-notify.org/astros.json")
        response.raise_for_status()
        astronauts_data = response.json()
        return [astronaut["name"] for astronaut in astronauts_data["people"]]
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch astronauts: {e}")
        return []


def main():
    while True:
        astronauts_list = fetch_astronauts()
        if astronauts_list:
            print("Astronauts currently in space:")
            for astronaut in astronauts_list:
                print(f"- {astronaut}")
        else:
            print("No data available.")

        time.sleep(10)


if __name__ == "__main__":
    main()
