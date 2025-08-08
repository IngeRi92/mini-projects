import random


def main():
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Genereerib suvalise arvu 1 ja 100 vahel
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        try:
            # usere sisestab oma arvu
            guess = int(
                input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: ")
            )
            attempts += 1

            # Kontrollib, kas kasutaja arv on õige
            if guess == secret_number:
                print(
                    f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!"
                )
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")

            # Aitab kasutajal jälgida järelejäänud katseid
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"You have {remaining} attempts remaining.")

        except ValueError:
            print("Please enter a valid number.")
            continue

    else:
        # katsed on lõppenud
        print(f"Game Over! The number was {secret_number}")

    # uuesti mängimine
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again in ["y", "yes"]:
        main()
    else:
        print("Thanks for playing!")


# Käivitub ainult otse jooksutamisel
if __name__ == "__main__":
    main()
