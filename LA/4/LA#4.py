print("Name: Moriah De Pedro")
print("=== LA #4 ====\n")

class hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role 
    
    def __str__(self):
        return "Miya is a Marksman hero"

legend = hero("Miya", "Marksman")
print(legend)