import random
from combat import combat

def start_game():
    name = input("\nEntrez votre nom : ")
    print(f"\nVotre nom est {name}. Vous vous réveillez au milieu d’une forêt avec un sac contenant un couteau.")
    current_location = "start"
    inventory = ["couteau"]
    health = 100
    xp = 0
    return current_location, inventory, health, xp

def describe_location(location):
    print(f"\n{map[location]}")

def move(location):
    print("\nDéplacez-vous en tapant : Go East, Go North, Go West, Go South.")
    direction = input("Que voulez-vous faire ? ").lower()
    
    if direction == "go east" and location == "start":
        return "forest1"
    elif direction == "go west" and location == "forest1":
        return "start"
    elif direction == "go east" and location == "forest1":
        return "forest2"
    elif direction == "go north" and location == "forest2":
        return "boss"
    else:
        print("\nVous ne pouvez pas aller dans cette direction.")
        return location

def game_loop():
    current_location, inventory, health, xp = start_game()
    
    while True:
        describe_location(current_location)
        
        if current_location == "boss":
            print("Le boss est ici. Préparez-vous pour le combat final !")
            health, xp, alive = combat(health, xp)
            if not alive:
                break
            print("Félicitations, vous avez vaincu le boss et gagné le jeu !")
            break
        
        event = random.choice(["combat", "objet", "rien"])
        if event == "combat":
            health, xp, alive = combat(health, xp)
            if not alive:
                break
        elif event == "objet":
            print("Vous avez trouvé une potion de soin. +20 points de vie.")
            health += 20
        
        current_location = move(current_location)
