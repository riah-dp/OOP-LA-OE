print("Name: Moriah De Pedro")
print("=== LA #23 ====\n")

class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def wrapper(*args, **kwargs):
            print("Introducing....")
            func(*args, **kwargs)
            print("This character is amazing!")
            return wrapper

taguro = AnimeCharacter("Sensui", "Spiritual Energy")

@taguro.introduce
def character_intro():
    print(f"I am {taguro.name} and I can use {taguro.ability}.")
character_intro()