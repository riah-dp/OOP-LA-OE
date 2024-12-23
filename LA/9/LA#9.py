print("Name: Moriah De Pedro")
print("=== LA #9 ====\n")

class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def __str__(self):
        return f"This car is a {self.brand}"
    
Adi = Car("Ford")
print(Adi)
print(Adi)
del Adi
print(Adi)