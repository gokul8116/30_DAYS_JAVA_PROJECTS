import random
import time

# Global leaderboard to store best scores for different players
leaderboard = {}

def show_leaderboard():
    if not leaderboard:
        print("\nLeaderboard is empty! Be the first to make it to the top!\n")
    else:
        print("\nLeaderboard:")
        sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1])
        for i, (player, score) in enumerate(sorted_leaderboard, 1):
            print(f"{i}. {player} - {score} attempts")
        print()

def show_score(attempts_list):
    if not attempts_list:
        print("There is currently no best score, it's yours for the taking!")
    else:
        print(f"The current best score is {min(attempts_list)} attempts")

def get_difficulty():
    while True:
        difficulty = input("\nChoose a difficulty level (Easy/Medium/Hard): ").lower()
        if difficulty in ['easy', 'medium', 'hard']:
            if difficulty == 'easy':
                return 10, 5
            elif difficulty == 'medium':
                return 10, 3
            else:
                return 20, 3
        else:
            print("Invalid choice. Please select Easy, Medium, or Hard.")

def start_game():
    print("\nWelcome to the Ultimate Number Guessing Game!")
    player_name = input("What is your name? ").capitalize()

    while True:
        max_num, max_attempts = get_difficulty()
        rand_num = random.randint(1, max_num)
        attempts = 0
        attempts_list = []
        
        show_leaderboard()
        show_score(attempts_list)

        while attempts < max_attempts:
            try:
                guess = int(input(f"\nPick a number between 1 and {max_num}: "))
                if guess < 1 or guess > max_num:
                    raise ValueError(f"Please guess a number within the range 1 to {max_num}.")

                attempts += 1

                if guess == rand_num:
                    print(f"\nCongratulations, {player_name}! You guessed the number in {attempts} attempts!")
                    attempts_list.append(attempts)
                    if player_name not in leaderboard or attempts < leaderboard[player_name]:
                        leaderboard[player_name] = attempts
                    break
                elif guess > rand_num:
                    print("Too high! Try again.")
                else:
                    print("Too low! Try again.")

                print(f"You have {max_attempts - attempts} attempts left.")
                time.sleep(0.5)  # Adds a slight delay for a better experience

            except ValueError as err:
                print(f"Invalid input: {err}. Please try again.")
        
        else:
            print(f"\nYou've run out of attempts! The correct number was {rand_num}. Better luck next time, {player_name}!")

        wanna_play = input("\nWould you like to play again? (Enter Yes/No): ").lower()
        if wanna_play != 'yes':
            print(f"\nThank you for playing, {player_name}! Here's the final leaderboard:")
            show_leaderboard()
            print("Goodbye!\n")
            break

if __name__ == '__main__':
    start_game()
