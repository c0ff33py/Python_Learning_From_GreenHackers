# Exercise 3: Methods
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        return f"{self.color} {self.brand} is driving..."


# Create car
car = Car("GTR", "Silver")

# Call method correctly
print(car.drive())  # ✅ Output: Silver GTR is driving...
