class Equipment:
    def __init__(self, name, attack_bonus=0, defense_bonus=0):
        self.name = name
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus

class Weapon(Equipment):
    def __init__(self, name, attack_bonus):
        super().__init__(name, attack_bonus=attack_bonus)

class Armor(Equipment):
    def __init__(self, name, defense_bonus):
        super().__init__(name, defense_bonus=defense_bonus)

class Accessory(Equipment):
    def __init__(self, name, attack_bonus=0, defense_bonus=0):
        super().__init__(name, attack_bonus=attack_bonus, defense_bonus=defense_bonus)
