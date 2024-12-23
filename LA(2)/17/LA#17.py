print("Name: Moriah De Pedro")
print("=== LA #17 ====\n")

class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacked {target.name} for {self.attack_power} damage.")
        print(f"{target.name}'s remaining health {target.name}")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name}, healed for {amount} health points.")
        print(f"{self.name}'s current health {self.health}")

adi = Player("Miya", 100, 150)
bal = Player("Brody", 150, 100)

while True:
    adi.attack(bal)

    if bal.health <= 0:
        print(f"{adi.name} wins!")
        break

adi.heal(10)
bal.heal(20)