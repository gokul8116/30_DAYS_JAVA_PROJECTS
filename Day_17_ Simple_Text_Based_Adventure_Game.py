def start_adventure():
    print("You find yourself in a dark forest.")
    choice1 = input("Do you want to go left or right? (left/right): ")

    if choice1 == "left":
        print("You encounter a wild beast!")
        choice2 = input("Do you fight or run? (fight/run): ")

        if choice2 == "fight":
            print("You bravely fight the beast and win!")
        else:
            print("You run away safely, but the adventure ends.")

    else:
        print("You find a hidden treasure!")
        choice3 = input("Do you open the chest or leave it? (open/leave): ")

        if choice3 == "open":
            print("The chest is filled with gold and jewels! You win!")
        else:
            print("You decide to leave the treasure and return home.")

if __name__ == "__main__":
    start_adventure()
