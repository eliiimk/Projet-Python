class Map:
    def __init__(self):
        # Carte fixe, aucun changement aléatoire
        self.locations = {
            "start": "Vous êtes au point de départ.",
            "forest": "Une forêt dense avec des bruits inquiétants.",
            "cave": "Une grotte sombre et humide.",
            "lake": "Un lac calme avec des eaux claires.",
            "mountain": "Une montagne abrupte avec une vue dégagée.",
            "boss": "Le Boss se tient ici, prêt à vous affronter."
        }
        self.player_position = "start"
    
    def move(self, direction):
        # Déplacements prédéfinis entre les emplacements
        moves = {
            "start": {"north": "forest"},
            "forest": {"south": "start", "east": "cave"},
            "cave": {"west": "forest", "north": "lake"},
            "lake": {"south": "cave", "east": "mountain"},
            "mountain": {"west": "lake", "north": "boss"},
            "boss": {}  # Aucun déplacement possible à partir du boss
        }
        if direction in moves[self.player_position]:
            self.player_position = moves[self.player_position][direction]
            print(f"Vous allez {direction}.")
        else:
            print("Vous ne pouvez pas aller dans cette direction.")
        return self.player_position

    def describe_location(self, location):
        print(self.locations.get(location, "Rien de spécial ici."))
