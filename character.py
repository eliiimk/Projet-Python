import random  # Import pour gérer les objets trouvés
from items import apply_item_effect

class Character:
    def __init__(self, name, character_class="Guerrier", hp=100, attack=10, defense=5, endurance=100):
        # Initialise le personnage avec des attributs de base
        self.name = name
        self.character_class = character_class
        self.hp = hp + (20 if character_class == "Guerrier" else 0)
        self.current_hp = self.hp
        self.attack = attack + (5 if character_class == "Mage" else 0)
        self.defense = defense + (3 if character_class == "Guerrier" else 0)
        self.endurance = endurance
        self.inventory = ["Potion", "Attack Boost", "Defense Boost"]  # Inventaire de base
        self.gold = 100
        self.xp = 0
        self.level = 1
        
    def gain_xp(self, amount):
        # Ajoute de l'XP et vérifie si un niveau supérieur est atteint
        self.xp += amount
        if self.xp >= self.level * 20:
            self.level_up()

    def level_up(self):
        # Augmente les caractéristiques au niveau supérieur
        self.level += 1
        self.max_hp += 20
        self.attack += 5
        self.defense += 3
        self.current_hp = self.max_hp
        print(f"{self.name} monte au niveau {self.level} !")

    def use_item(self, item):
        # Utilise un objet et applique son effet
        apply_item_effect(self, item)
        self.inventory.remove(item)

    def find_item(self):
        # Ajoute un objet aléatoire à l'inventaire
        item = random.choice(["Potion", "Attack Boost", "Defense Boost"])
        self.inventory.append(item)
        print(f"Vous avez trouvé un {item}!")
