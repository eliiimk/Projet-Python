class Monster:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.max_hp = level * 20 + 50
        self.current_hp = self.max_hp
        self.attack = level * 5 + 10
        self.defense = level * 3 + 5
