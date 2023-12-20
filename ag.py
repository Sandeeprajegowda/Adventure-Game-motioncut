import time

def introduction():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious place.")
    time.sleep(1)
    print("Your goal is to navigate through the challenges and reach the treasure.")
    time.sleep(1)
    print("Let the adventure begin!\n")

def choose_path():
    print("Choose your path:")
    print("1. Go left")
    print("2. Go right")
    return input("Enter 1 or 2: ")

def encounter_monster():
    print("Oh no! You've encountered a fierce monster!")
    time.sleep(1)
    print("What will you do?")
    print("1. Fight")
    print("2. Run")
    return input("Enter 1 or 2: ")

def treasure_room():
    print("Congratulations! You've reached the treasure room.")
    time.sleep(1)
    print("You've successfully completed the adventure!")

def main():
    introduction()

    # First decision
    path_choice = choose_path()

    if path_choice == "1":
        print("You chose to go left.")
        time.sleep(1)
        # Encounter a monster
        monster_choice = encounter_monster()

        if monster_choice == "1":
            print("You chose to fight the monster.")
            time.sleep(1)
            print("Unfortunately, the monster was too strong. Game over!")
        elif monster_choice == "2":
            print("You chose to run away.")
            time.sleep(1)
            print("You narrowly escaped the monster and continue your journey.")
            # Continue the story...

    elif path_choice == "2":
        print("You chose to go right.")
        time.sleep(1)
        # Continue the story...

    else:
        print("Invalid choice. Game over!")

if __name__ == "__main__":
    main()
