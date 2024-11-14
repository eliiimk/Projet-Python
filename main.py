from character import Character    # Importation de la classe pour créer un joueur
from map import Map                # Importation de la classe pour gérer la carte
from utils import save_game, load_game  # Importation des fonctions de sauvegarde et de chargement
from combat import encounter  
from store import Store       # Importation de la fonction de combat
import random                       # Pour les choix aléatoires

def main_menu():
    # Affiche le menu principal et renvoie le choix du joueur
    print("\nMAIN MENU:")
    print("1. Créer une nouvelle partie")
    print("2. Charger une partie sauvegardée")
    print("3. À propos")
    print("4. Quitter")
    return input("Choisissez une option : ")

def choose_class():
    print("Choisissez une classe :")
    print("1. Guerrier - Plus de HP, meilleure défense")
    print("2. Mage - Attaque magique élevée, moins de HP")
    print("3. Voleur - Attaque équilibrée, esquive")
    choice = input("Classe : ")
    if choice == "1":
        return "Guerrier"
    elif choice == "2":
        return "Mage"
    elif choice == "3":
        return "Voleur"
    else:
        print("Choix invalide, Guerrier choisi par défaut.")
        return "Guerrier"

def start_game():
    # Démarre une nouvelle partie
    player_name = input("Entrez votre nom : ")
    player_class = choose_class()
    player = Character(name=player_name, character_class=player_class) # Crée un personnage
    game_map = Map()                      # Crée une carte
    print(f"Bienvenue dans l'aventure, {player_name} le {player_class}!")
    game_loop(player, game_map)           # Appelle la boucle de jeu principale

def game_loop(player, game_map):
    store = Store()
    # Boucle de jeu principale où le joueur entre des commandes
    while player.current_hp > 0:  # Tant que le joueur a de la vie
        print("\nDirection actuelle :")
        print("Commandes : Go North, Go South, Go East, Go West, store, Menu")
        command = input("Votre commande : ").lower()  # Récupère la commande

        if command == "menu":
            save_game(player)  # Sauvegarde et quitte si "menu" est entré
            break
        elif command == "store":
            store.visit(player)
        elif command in ["go north", "go south", "go east", "go west"]:
            location = game_map.move(command)
            game_map.describe_location(location)
            
            # Rencontre aléatoire sauf au départ ou au boss
            if random.random() < 0.5 and location not in ["start", "boss"]:
                if random.random() < 0.5:
                    encounter(player)                 # Déclenche un combat
                else:
                    print("Vous trouvez un objet !")
                    player.find_item()                # Le joueur trouve un objet
            if location == "boss":
                print("Le Boss vous attend...")
                if encounter(player, boss=True):      # Combat final avec le boss
                    print("Félicitations ! Vous avez vaincu le Boss !")
                    break
        else:
            print("Commande inconnue.")

    if player.current_hp <= 0:
        print("Vous avez été vaincu. Retour au menu principal.")


if __name__ == "__main__":
    while True:
        choice = main_menu()  # Affiche le menu principal
        if choice == "1":
            start_game()      # Nouvelle partie
        elif choice == "2":
            player = load_game()     # Charge une partie
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
