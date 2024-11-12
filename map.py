class Map:
    def __init__(self):
        self.locations = {
            "start": "Vous êtes au départ, dans une clairière calme.",
            "forest1": "Vous entrez dans une forêt dense.",
            "forest2": "Des arbres sombres et imposants vous entourent.",
            "boss": "Vous êtes face au Boss, prêt pour le combat final."
        }
        self.current_location = "start"

    def move(self, direction):
        if direction == "go north":
            self.current_location = "forest1"
        elif direction == "go east":
            self.current_location = "forest2"
        elif direction == "go west":
            self.current_location = "start"
        elif direction == "go south" and self.current_location == "forest2":
            self.current_location = "boss"
        return self.current_location

    def describe_location(self, location):
        print(self.locations.get(location, "Endroit inconnu."))
