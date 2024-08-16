import random

choices = ["Rock", "Paper", "Scissors"]
cpu_score = 0
player_score = 0

while True:
    computer = random.choice(choices)
    player = input("Rock, Paper, or Scissors? (or type 'End' to quit): ").capitalize()

    if player == "End":
        print("Final Scores:")
        print(f"CPU: {cpu_score}")
        print(f"Player: {player_score}")
        break

    if player not in choices:
        print("Invalid choice! Please choose Rock, Paper, or Scissors.")
        continue

    if player == computer:
        print(f"Tie! Both chose {player}.")
    elif player == "Rock":
        if computer == "Paper":
            print(f"You lose! {computer} covers {player}.")
            cpu_score += 1
        else:
            print(f"You win! {player} smashes {computer}.")
            player_score += 1
    elif player == "Paper":
        if computer == "Scissors":
            print(f"You lose! {computer} cuts {player}.")
            cpu_score += 1
        else:
            print(f"You win! {player} covers {computer}.")
            player_score += 1
    elif player == "Scissors":
        if computer == "Rock":
            print(f"You lose! {computer} smashes {player}.")
            cpu_score += 1
        else:
            print(f"You win! {player} cuts {computer}.")
            player_score += 1