print("Name: Moriah De Pedro")
print("=== LA #11 ====\n")

class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describePhone(self):
        print(f"The Phone's brand is {self.brand} and the Model is {self.model}")

class Android(Phone):
    def __init__(self, brand, model):
        Phone.__init__(self, brand, model)

Vivo = Android("Vivo", "V14")
Vivo.describePhone()