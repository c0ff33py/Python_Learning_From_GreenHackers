# Exercise 2: constructior
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

# Create an object with data


my_car = Car("Suzuki", "Brown")
print(f'{my_car.brand} color is {my_car.color}')
