print("Name: Moriah De Pedro")
print("=== LA #21 ====\n")

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
    
    def may_chicken_ba(self, age):
        if age >= 15:
            return self.__chicken
        else:
            return "secret!"
        
    def i_set_to(self, new):
        self.__chicken = new
        
chicken_curry = FavoriteFood("chicken", "potato", "carrot", "coconut", "pepper", "salt", "currypowder")
chicken_curry.i_set_to("Buong Chicken")
print(chicken_curry.may_chicken_ba(50))