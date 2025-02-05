import sys

print("Welcome to the RPG Game!")
print("Choose your class: 1. Warrior 2. Mage 3. Healer")
classSelect = int(input("Enter the number of your class (1/2/3): "))
match classSelect:
    case 1:
        print("You have chosen Warrior! You are strong and brave.")
        print("What would you like to do? 1. Attack with your sword 2. Defend with your shield.")
        choice = int(input("Choose your action (1/2): "))
        match choice:
            case 1:
                print("You swing your sword and defeat the enemy!")
                print("Thank you for playing!")
            case 2:
                print("You raise your shield and block the enemy's attack!")
                print("Thank you for playing!")
            case _:
                print("Invalid action choice. The game ends.")
                print("Thank you for playing!")
                sys.exit()
    case 2:
        print("You have chosen Mage! You wield powerful magic.")
        print("What would you like to do? 1. Cast a fireball 2. Cast a healing spell")
        choice = int(input("Choose your action (1/2): "))
        match choice:
            case 1:
                print("You cast a fireball and scorch the enemy!")
                print("Thank you for playing!")
            case 2:
                print("You cast a healing spell and restore your energy.")
                print("Thank you for playing!")
            case _:
                print("Invalid action choice. The game ends.")
                print("Thank you for playing!")
                sys.exit()
    case 3:
        print("You have chosen Healer! You are kind and supportive.")
        print("What would you like to do? 1. Heal your ally 2. Attack with your staff")
        choice = int(input("Choose your action (1/2): "))
        match choice:
            case 1:
                print("You heal your ally and boost their morale!")
                print("Thank you for playing!")
            case 2:
                print("You swing your staff and knock out the enemy!")
                print("Thank you for playing!")
            case _:
                print("Invalid action choice. The game ends.")
                print("Thank you for playing!")
                sys.exit()
    case _:
        print("Invalid class choice. The game ends.")
        print("Thank you for playing!")
        sys.exit()

