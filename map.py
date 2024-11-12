class Map:
    def __init__(self):
        self.locations = {
            "start": "Vous êtes au point de départ.",
            "dungeon_level_1": "Vous êtes dans le premier niveau du donjon.",
            "dungeon_level_2": "Un couloir sombre avec des bruits étranges.",
            "dungeon_level_3": "Vous sentez une forte présence magique ici.",
            "boss": "Le Boss est ici, une aura puissante émane."
        }
        self.player_position = "start"

    def move(self, direction):
        # Gère les niveaux de donjon en fonction des directions
        if direction in ["north", "south", "east", "west"]:
            # Ajout de logique pour changer les niveaux du donjon
            self.player_position = "dungeon_level_1"  # Exemple simple
        return self.player_position

    def describe_location(self, location):
        print(self.locations.get(location, "Rien de spécial ici."))
