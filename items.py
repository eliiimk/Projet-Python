def apply_item_effect(character, item):
    if item == "Potion":
        character.current_hp = min(character.max_hp, character.current_hp + 30)
        print(f"{character.name} utilise une Potion et regagne de la vie.")
    elif item == "Attack Boost":
        character.attack += 10
        print(f"{character.name} utilise un Attack Boost.")
    elif item == "Defense Boost":
        character.defense += 5
        print(f"{character.name} utilise un Defense Boost.")
