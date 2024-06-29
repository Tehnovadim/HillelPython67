import requests
from typing import List, Dict


def get_zoo_data() -> List[Dict]:
    url = 'https://script.google.com/macros/s/AKfycbyJpvxIeUYvPnEVgPIGq_IkF89klY_0eVCtCPWdOq_soqx4D-7_C9ePkvDsyeeSMLyC/exec'
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data, status code: {response.status_code}")

    data = response.json()
    if 'error' in data:
        raise Exception(f"API error: {data['error']}")

    return data['animals']


def calculate_poisonous_care_cost(data: List[Dict]) -> float:
    total_cost = 0.0

    for item in data:
        try:
            if item['is_poisonous']:
                care_cost = float(item['care_cost'])
                number_of_animals = int(item['number_of_animals'])
                total_cost += care_cost * number_of_animals
        except (ValueError, KeyError) as e:
            print(f"Skipping row due to error: {e}")
            continue

    return round(total_cost, 2)


def count_african_animals(data: List[Dict]) -> int:
    count = 0

    for item in data:
        try:
            if item['continent'].lower() == 'африка':
                count += int(item['number_of_animals'])
        except (ValueError, KeyError) as e:
            print(f"Skipping row due to error: {e}")
            continue

    return count


def main():
    try:
        zoo_data = get_zoo_data()

        poisonous_care_cost = calculate_poisonous_care_cost(zoo_data)
        print(f"Total care cost for poisonous animals: ${poisonous_care_cost}")

        african_animals_count = count_african_animals(zoo_data)
        print(f"Total number of African animals in the zoo: {african_animals_count}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
