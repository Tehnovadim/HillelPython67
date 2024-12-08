class Car:
    def __init__(self, year=2020, manufacturer=None, model=None, fuel_consumption=0.0):
        self.year = year
        self.manufacturer = manufacturer
        self.model = model
        self.mileage = 0
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return f'{self.year} {self.manufacturer} {self.model} with {self.mileage} km and {self.fuel_consumption} l/100km'

car1 = Car(year=2021, manufacturer='Toyota', model='Corolla', fuel_consumption=6.5)
car2 = Car(year=2019, manufacturer='Ford', model='Mustang', fuel_consumption=9.8)
car3 = Car(year=2020, manufacturer='Tesla', model='Model 3', fuel_consumption=0)

print(car1)
print(car2)
print(car3)