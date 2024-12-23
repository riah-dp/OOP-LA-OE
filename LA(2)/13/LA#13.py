print("Name: Moriah De Pedro")
print("=== LA #13 ====\n")

class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class Fish(Animal):
    def __init__(self, name, type, can_swim):
        self._can_swim = can_swim


fish = Fish("Namsin", "Bangus", True)
print(fish._can_swim)