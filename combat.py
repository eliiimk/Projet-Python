import random
from monster import Monster

def encounter(player, boss=False):
    monster = Monster("Boss" if boss else "Goblin", level=player.level + (2 if boss else 0))
    print(f"Vous rencontrez un {monster.name} de niveau {monster.level} avec {monster.max_hp} HP !")
    
    while player.current_hp > 0 and monster.current_hp > 0:
        action = input("Que voulez-vous faire ? (attack/use item/run) ").lower()
        
        if action == "attack":
            damage = max(0, player.attack - monster.defense)
            monster.current_hp -= damage
            print(f"{player.name} inflige {damage} dégâts à {monster.name} !")
        elif action == "use item":
            print(f"Inventaire : {player.inventory}")
            item = input("Objet : ")
            if item in player.inventory:
                player.use_item(item)
        elif action == "run":
            print("Vous fuyez le combat.")
            return False
        else:
            continue

        if monster.current_hp > 0:
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
