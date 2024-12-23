print("Name: Moriah De Pedro")
print("=== LA #19 ====\n")

class FavoriteFood:
    def __init__(self, chicken, potato, carrot, coconut, pepper, salt, currypowder):
        self.__chicken = chicken
        self.__potato = potato
        self.__carrot = carrot
        self.__coconut = coconut
        self.__pepper = pepper
        self.__salt = salt
        self.__currypowder = currypowder

    def __str__(self):
        return f"My Chicken Curry has {self.__chicken}, {self.__potato}, {self.__carrot}, {self.__coconut}, {self.__pepper}, {self.__salt}, {self.__currypowder}"
    
chicken_curry = FavoriteFood("chicken", "potato", "carrot", "coconut", "pepper", "salt", "currypowder")

print(chicken_curry.__chicken)