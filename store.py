class Store:
    def __init__(self):
        self.items = {
            "potion": {"price": 10, "effect": "restore_hp"},
            "attack_boost": {"price": 15, "effect": "increase_attack"},
            "defense_boost": {"price": 15, "effect": "increase_defense"},
        }

    def visit(self, player):
        print("\nBienvenue dans la boutique !")
        print(f"Or actuel : {player.gold} pièces")
        for item, details in self.items.items():
            print(f"{item.capitalize()} - {details['price']} pièces")

        choice = input("Quel objet voulez-vous acheter ? (Tapez 'quitter' pour partir) : ").lower()
        if choice in self.items:
            item = self.items[choice]
            if player.gold >= item["price"]:
                player.gold -= item["price"]
                player.inventory.append(choice)
                print(f"Vous avez acheté {choice.capitalize()} !")
            else:
                print("Pas assez d'or.")
        elif choice == "quitter":
            print("Merci pour votre visite !")
        else:
            print("Objet non disponible.")
