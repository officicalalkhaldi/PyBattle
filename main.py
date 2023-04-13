from random import choice
from typing import Tuple

GAME_TITLE = """
  __        __                       
 /  | /  ||/  |      /    /    /     
(___|(___||___| ___ (___ (___ (  ___ 
|        )|   )|   )|    |    | |___)
|     __/ |__/ |__/||__  |__  | |__  
"""

# Function to display the game title
def display_title(title: str = "") -> None:
    """
    Displays the game title on the console.
    
    Args:
    title (str): The title to be displayed.
    """
    print(title.center(60))
    print("=" * 60)
    print()

# Function to play a round of the game
def play_round(player_choice: int, player_score: int, computer_score: int) -> Tuple[int, int, str]:
    """
    Plays one round of the game and returns the updated scores and computer's choice.
    
    Args:
    player_choice (int): The player's choice (1 for rock, 2 for paper, 3 for scissors).
    player_score (int): The player's current score.
    computer_score (int): The computer's current score.
    
    Returns:
    tuple[int, int, str]: The updated player and computer scores, and the computer's choice.
    """
    choices = {1: "rock", 2: "paper", 3: "scissors"}
    computer_choice = choices[choice([1, 2, 3])]
    if player_choice == 1 and computer_choice == "scissors" or \
        player_choice == 2 and computer_choice == "rock" or \
        player_choice == 3 and computer_choice == "paper":
        player_score += 1
        result = choices[player_choice] + " beats " + computer_choice + "."
    elif player_choice == 1 and computer_choice == "paper" or \
        player_choice == 2 and computer_choice == "scissors" or \
        player_choice == 3 and computer_choice == "rock":
        computer_score += 1
        result = computer_choice + " beats " + choices[player_choice] + "."
    else:
        result = "It's a tie!"
    print(f"\n{result}\n[ Player: {player_score} | Computer: {computer_score} ]\n\n")
    return player_score, computer_score, computer_choice

# Main program
def main() -> None:
    """
    The main program loop for the Rock, Paper, Scissors game.
    """
    # Initialize scores
    player_score = 0
    computer_score = 0
    
    # Display game title
    display_title(GAME_TITLE)
    
    # Prompt user to start a new game or continue with existing scores
    while True:
        choice_of = input("Enter 'n' to start a new game with fresh scores, or 'c' to continue with existing scores: ")
        print("\n" + "=" * 60 + "\n" * 2)
        if choice_of == "n":
            player_score = 0
            computer_score = 0
            break
        elif choice_of == "c":
            break
        else:
            print("Invalid input")
    
    # Game loop
    while True:
        pp = input("Enter your choice (1 for rock, 2 for paper, 3 for scissors, q to quit): ")
        if pp == "q":
            # Save scores to file and exit game
            with open("scores.txt", "w") as f:
                f.write(f"Player: {player_score}\n")
                f.write(f"Computer: {computer_score}\n")
            print("\n\n\n=======================\n" + "\n  Final scores:  ")
            print(f"\n   Player: {player_score}")
            print(f"   Computer: {computer_score}")
            print("\n=======================\n\n")
            break
        elif pp == "1" or pp == "2" or pp == "3":
            player_choice = int(pp)
            player_score, computer_score, computer_choice = play_round(player_choice, player_score, computer_score)
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
