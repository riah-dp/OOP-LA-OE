print("Name: Moriah De Pedro")
print("=== OE#4 ===")

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
    def attack(self, target):
        target.health -= self.power
        print(f"{self.name} attacks {target.name}, reducing their health to {target.health}!")

    def special_move(self):
        pass

    def defend(self, attacker):
        reduced_damage = max(0, attacker.power - 5) # Reduces damage by 5
        self.health -= reduced_damage
        print(f"{self.name} defends, reducing damage to {reduced_damage} Health is now {self.health}.")

class Warrior(Character):
    def special_move(self):
        print(f"{self.name} uses Shield Bash!")
        self.power *= 2 # Double attack power temporarily

class Mage(Character):
    def special_move(self):
            print(f"{self.name} casts Fireball!")
            self.power = 100 # Fixed high damage for next attack
class Archer(Character):
    def special_move(self):
            print(f"{self.name} shoots a Piercing Arrow!")
            self.power += 15 # Temporarily increases power
class Monster(Character):
    def special_move(self):
        print(f"{self.name} roars and gains extra health!")
        self.health += 50
# Initialize characters
warrior = Warrior("Warrior", 200, 20)
mage = Mage("Mage", 150, 30)
archer = Archer("Archer", 180, 25)
monster = Monster("Monster", 300, 40)
characters = [warrior, mage, archer, monster]
# Battle simulation
print("\n--- Characters attack Monster ---")
for char in characters[:-1]:
    char.attack(monster)
    char.special_move()
print("\n--- Monster retaliates ---")
for char in characters[:-1]:
    monster.attack(char)
    monster.special_move()
print("\n--- Demonstrating polymorphism ---")
for char in characters:
    char.special_move()