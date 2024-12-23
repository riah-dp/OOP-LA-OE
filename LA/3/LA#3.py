print("Name: Moriah De Pedro")
print("=== LA #3 ====\n")

class hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role 
    
    def describe(self):
        print(f"{self.name} is a {self.role} hero")

legend = hero("Miya", "Marksman")
legend.describe()