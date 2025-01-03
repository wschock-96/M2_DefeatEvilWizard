from classes import Warrior, Mage, Archer, Paladin
from evil_wizard import EvilWizard
from character import Character

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Character):
                    player.special_ability(wizard)
        elif choice == '3':
            player.health_regen()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        # Handle wizard's turn
        if wizard.health > 0:
            wizard.regenerate()

            if player.defense_active:
                player.defense_active = False
            else:
                wizard.attack(player)

        if player.health <= 0:
            print(f"Defeat! {player.name} has been slain!")
            break

    if wizard.health <= 0:
        print(f"Victory! The {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
