class NPC:
    def __init__(self, name, dialogue, hint=None):
        self.name = name
        self.dialogue = dialogue
        self.hint = hint

    def talk(self):
        print(f"{self.name} : {self.dialogue}")
        if self.hint:
            print(f"Indice : {self.hint}")
