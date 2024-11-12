from equipment import Weapon, Armor, Accessory

class Character:
    def __init__(self, name, character_class="Guerrier", hp=100, attack=10, defense=5, endurance=100):
        self.name = name
        self.character_class = character_class
        self.hp = hp + (20 if character_class == "Guerrier" else 0)
        self.current_hp = self.hp
        self.attack = attack + (5 if character_class == "Mage" else 0)
        self.defense = defense + (3 if character_class == "Guerrier" else 0)
        self.endurance = endurance
        self.inventory = []
        self.journal = []
        self.gold = 100  # Nouveau : ajouter de l'or
        self.equipped_weapon = None
        self.equipped_armor = None
        self.equipped_accessory = None
        self.xp = 0
        self.level = 1

    def add_to_journal(self, entry):
        self.journal.append(entry)
        print(f"Journal mis à jour : {entry}")

    def equip(self, item):
        # Equipement de différents types d'objets
        pass

    def find_item(self):
        # Ajoute un objet à l'inventaire
        pass

    def gain_xp(self, amount):
        # XP et progression de niveau
        pass
