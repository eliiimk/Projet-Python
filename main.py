from character import Character
from map import Map
from utils import save_game, load_game
from combat import encounter
import random

def main_menu():
    print("\nMAIN MENU:")
    print("1. Créer une nouvelle partie")
    print("2. Charger une partie sauvegardée")
    print("3. À propos")
    print("4. Quitter")
    return input("Choisissez une option : ")

def start_game():
    player_name = input("Entrez votre nom : ")
    player = Character(name=player_name)
    game_map = Map()
    print("Bienvenue dans l'aventure, {} !".format(player_name))
    game_loop(player, game_map)

def game_loop(player, game_map):
    while player.current_hp > 0:
        print("\nDirection actuelle :")
        print("Commandes : Go North, Go South, Go East, Go West, Menu")

        command = input("Votre commande : ").lower()
        if command == "menu":
            save_game(player)
            break
        elif command in ["go north", "go south", "go east", "go west"]:
            location = game_map.move(command)
            game_map.describe_location(location)
            
            # Aléatoirement rencontrer un monstre ou trouver un objet
            if random.random() < 0.5 and location not in ["start", "boss"]:
                if random.random() < 0.5:
                    encounter(player)
                else:
                    print("Vous trouvez un objet !")
                    player.find_item()
                    
            if location == "boss":
                print("Le Boss vous attend...")
                if encounter(player, boss=True):
                    print("Félicitations ! Vous avez vaincu le Boss !")
                    break
        else:
            print("Commande inconnue.")

if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == "1":
            start_game()
        elif choice == "2":
            player = load_game()
            if player:
                game_map = Map()
                game_loop(player, game_map)
        elif choice == "3":
            print("\nRPG en console écrit en Python par Eli & Michel.")
        elif choice == "4":
            print("Merci d'avoir joué !")
            break
        else:
            print("Choix invalide.")
