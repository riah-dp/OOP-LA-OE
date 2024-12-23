print("Name: Moriah De Pedro")
print("=== LA #24 ====\n")

from abc import ABC, abstractmethod

class GameCharacter(ABC):
    @abstractmethod
    def attack(self):
        pass

class Warrior(GameCharacter):
    def attack(self):
        print("Swing sword!")

class Mage(GameCharacter):
    def attack(self):
        print("Cast a fireball!")

class Archer(GameCharacter):
    def attack(self):
        print("Shoots an arrow!")

warrior = Warrior()
warrior.attack()

mage = Mage()
mage.attack()

archer = Archer()
archer.attack()

class Healer(GameCharacter):
    def attack(self):
        print("Cast a healing spell on ally!")

healer = Healer()
healer.attack()