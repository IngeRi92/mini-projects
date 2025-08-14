import random


# Mängija valib oma käigu
def get_player_choice():
    choices = {"r": "rock", "p": "paper", "s": "scissors"}
    while True:
        user_input = (
            input("Enter your choice (rock/paper/scissors or r/p/s): ").lower().strip()
        )
        if user_input in choices:
            return choices[user_input]
        if user_input in choices.values():
            return user_input
        print("Invalid choice. Please enter rock, paper, scissors (or r, p, s).")


# Arvuti valib juhusliku käigu
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


# Määrab võitja
def determine_winner(player, computer):
    if player == computer:
        return "tie"
    wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    return "player" if wins[player] == computer else "computer"


# Kuvab tulemuse ja seletuse
def display_result(result, player, computer):
    explanations = {
        ("rock", "scissors"): "Rock crushes scissors",
        ("paper", "rock"): "Paper covers rock",
        ("scissors", "paper"): "Scissors cut paper",
        ("scissors", "rock"): "Rock crushes scissors",
        ("rock", "paper"): "Paper covers rock",
        ("paper", "scissors"): "Scissors cut paper",
    }
    print(f"\nYou chose: {player.capitalize()}")
    print(f"Computer chose: {computer.capitalize()}")
    if result == "tie":
        print("It's a tie!")
    elif result == "player":
        print(f"You win! {explanations.get((player, computer), '')}")
    else:
        print(f"Computer wins! {explanations.get((player, computer), '')}")


# Põhifunktsioon, mis juhib mängu
def main():
    print("Welcome to Rock Paper Scissors!")
    print("Rules: Rock crushes Scissors, Scissors cut Paper, Paper covers Rock")
    print("You can use shortcuts: r = rock, p = paper, s = scissors")
    player_score = computer_score = ties = 0
    round_number = 1

    while True:
        print(f"\n{'='*50}\nROUND {round_number}\n{'='*50}")
        player = get_player_choice()
        computer = get_computer_choice()
        result = determine_winner(player, computer)
        display_result(result, player, computer)
        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1
        else:
            ties += 1
        print(
            f"\nCurrent Score:\nYou: {player_score}\nComputer: {computer_score}\nTies: {ties}"
        )
        round_number += 1
        if input(
            "\nDo you want to play another round? (y/n): "
        ).lower().strip() not in ["y", "yes"]:
            break

    print(f"\n{'='*50}\nGAME OVER - FINAL RESULTS\n{'='*50}")
    print(f"Total rounds played: {round_number - 1}")
    print(f"Your wins: {player_score}\nComputer wins: {computer_score}\nTies: {ties}")
    if player_score > computer_score:
        print("Congratulations! You won overall!")
    elif computer_score > player_score:
        print("Computer won overall. Better luck next time!")
    else:
        print("It's a tie overall! Great game!")
    if player_score + computer_score > 0:
        print(
            f"Your win rate: {(player_score / (player_score + computer_score)) * 100:.1f}%"
        )
    print("Thanks for playing Rock Paper Scissors!")


# Käitab mängu
if __name__ == "__main__":
    main()
