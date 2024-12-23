print("Name: Moriah De Pedro")
print("=== LA #7 ====\n")

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

adi = Car("Ford", "Blue")
print(adi.brand, adi.color)
adi.color = "Black"

bal = Car("BMW", "Black")
print(bal.brand, bal.color)