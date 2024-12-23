print("Name: Moriah De Pedro")
print("=== OE #1 ===\n")

class hero():
    def __init__(self, name, role, dmg_type, health, auto_atk_dmg):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type
        self.health = health
        self.auto_atk_dmg = auto_atk_dmg
    def describe(self):
        return f"{self.name} is a {self.role} with a {self.dmg_type} power."
hero_mm1 = hero("Miya", "Marksman", "Attack Damage", "2490", "115")
hero_fighter1 = hero("Alpha", "Fighter", "Attack Damage", "2689", "123")
hero_mg1 = hero("Eudora", "Mage", "Magic Damage", "2496", "130")
hero_ass1 = hero("Gusion", "Assasin", "Attack Damage", "2429", "117")
hero_sup1 = hero("Floryn", "Support", "Magic Damage", "2468", "115")
print(f'''
{hero_mm1.name}
{hero_mm1.role}
{hero_mm1.dmg_type}
{hero_mm1.health} HP
{hero_mm1.auto_atk_dmg} basic attack damage
{hero_mm1.describe()}
{hero_fighter1.name}
{hero_fighter1.role}
{hero_fighter1.dmg_type}
{hero_mm1.health} HP
{hero_mm1.auto_atk_dmg} basic attack damage
{hero_fighter1.describe()}
{hero_mg1.name}
{hero_mg1.role}
{hero_mg1.dmg_type}
{hero_mm1.health} HP
{hero_mm1.auto_atk_dmg} basic attack damage
{hero_mg1.describe()}
{hero_ass1.name}
{hero_ass1.role}
{hero_ass1.dmg_type}
{hero_mm1.health} HP
{hero_mm1.auto_atk_dmg} basic attack damage
{hero_ass1.describe()}
{hero_sup1.name}
{hero_sup1.role}
{hero_sup1.dmg_type}
{hero_mm1.health} HP
{hero_mm1.auto_atk_dmg} basic attack damage
{hero_sup1.describe()} ''')