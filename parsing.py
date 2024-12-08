import pandas as pd

file_path = 'D:/user/Downloads/airport-codes_csv.csv'
df = pd.read_csv(file_path, delimiter=';', on_bad_lines='skip')

ukraine_airports = df[df['iso_country'] == 'UA']
ukraine_airport_names = ukraine_airports['name'].tolist()

for name in ukraine_airport_names:
    print(name)
