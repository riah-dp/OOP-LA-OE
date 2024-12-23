print("Name: Moriah De Pedro")
print("=== LA #10 ====\n")

class Vehicle:
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def describeVehicle(self):
        print(f"My Vehicle Brand is {self.brand} and the Model is {self.model} with {self.fuel_type} fuel type\n")

class Car(Vehicle):
    pass

adi = Car("Ford", "Ford Mustang", "Gasoline")
(adi.describeVehicle())

print("======================================================================\n")

class Motorcycle(Vehicle):
    pass
bal = Motorcycle("Ducati", "Ducati Diavel V4", "Gasoline")
(bal.describeVehicle())