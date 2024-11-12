import pickle

def save_game(player):
    with open("savefile.pkl", "wb") as file:
        pickle.dump(player, file)
    print("Jeu sauvegardé.")

def load_game():
    try:
        with open("savefile.pkl", "rb") as file:
            player = pickle.load(file)
            print("Jeu chargé.")
            return player
    except FileNotFoundError:
        print("Aucune sauvegarde trouvée.")
        return None
