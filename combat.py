import random
from monster import Monster

def encounter(player, boss=False):
    # Crée un monstre ou le boss et lance le combat
    monster = Monster("Boss" if boss else "Goblin", level=player.level + (2 if boss else 0))
    print(f"Vous rencontrez un {monster.name} de niveau {monster.level} avec {monster.max_hp} HP !")

    while player.current_hp > 0 and monster.current_hp > 0:
        # Affiche les options de combat
        action = input("Que voulez-vous faire ? (attack/use item/run) ").lower()
        
        if action == "attack":
            # Le joueur attaque et inflige des dégâts au monstre
            damage = max(0, player.attack - monster.defense)
            monster.current_hp -= damage
            print(f"{player.name} inflige {damage} dégâts à {monster.name} !")
        elif action == "use item":
            # Utilisation d'un objet dans l'inventaire
            print(f"Inventaire : {player.inventory}")
            item = input("Objet : ")
            if item in player.inventory:
                player.use_item(item)
        elif action == "run":
            print("Vous fuyez le combat.")
            return False

        if monster.current_hp > 0:
            # Le monstre attaque
            monster_damage = max(0, monster.attack - player.defense)
            player.current_hp -= monster_damage
            print(f"{monster.name} attaque et inflige {monster_damage} dégâts.")
        
        if player.current_hp <= 0:
            print("Vous avez perdu le combat.")
            return False
        elif monster.current_hp <= 0:
            print(f"Vous avez vaincu {monster.name} !")
            player.gain_xp(monster.level * 10)
            return True
