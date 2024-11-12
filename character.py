import random
from items import apply_item_effect

class Character:
    def __init__(self, name, level=1, hp=100, attack=10, defense=5, xp=0):
        self.name = name
        self.level = level
        self.max_hp = hp
        self.current_hp = hp
        self.attack = attack
        self.defense = defense
        self.xp = xp
        self.inventory = ["Potion", "Attack Boost", "Defense Boost"]

    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= self.level * 20:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.max_hp += 20
        self.attack += 5
        self.defense += 3
        self.current_hp = self.max_hp
        print(f"{self.name} monte au niveau {self.level} !")

    def use_item(self, item):
        apply_item_effect(self, item)
        self.inventory.remove(item)

    def find_item(self):
        item = random.choice(["Potion", "Attack Boost", "Defense Boost"])
        self.inventory.append(item)
        print(f"Vous avez trouvé un {item}!")
