"""A short text-based adventure game with exploration, choices, and scoring."""

import random


def intro_game():
    """Welcome the player and collect their name.

    Returns:
        str: The player's chosen name.
    """
    print("Welcome to Moonlit Mystery!")
    name = input("What is your name? ").strip()
    if not name:
        name = "Traveler"
    print(
        f"\nWelcome, {name}! Your adventure begins at the edge of a mysterious island.\n"
    )
    return name


def show_story(scene):
    """Display the current scene description for the player.

    Args:
        scene (str): The narrative text for the current location.

    Returns:
        None.
    """
    print(scene)


def get_choice(options):
    """Prompt the player until they provide a valid menu option.

    Args:
        options (dict): A mapping of numeric options to their descriptions.

    Returns:
        int: The valid selected choice.
    """
    while True:
        choice = input(f"\nPick a choice ({min(options)}-{max(options)}): ").strip()
        try:
            selection = int(choice)
            if selection in options:
                return selection
        except ValueError:
            pass
        print("Invalid choice. Please select one of the listed options.")


def handle_event(player, location):
    """Resolve the event at the player's current location.

    Args:
        player (dict): State for the current game, including health and treasure.
        location (str): The name of the active location.

    Returns:
        bool: True if the adventure continues, False if the game should end.
    """
    if location == "Whispering Forest":
        print(
            "\nYou hear whispers in the fog and notice a silver lantern glowing nearby."
        )
        print("1) Follow the lanterns")
        print("2) Walk across the old bridge")
        print("3) Search the bushes for clues")
        choice = get_choice({1: "Follow", 2: "Bridge", 3: "Bushes"})

        if choice == 1:
            print(
                "You follow the lanterns to a hidden clearing and find a pouch of gold."
            )
            player["gold"] += 15
        elif choice == 2:
            print("The bridge creaks under your feet, and a hidden trap injures you.")
            player["health"] -= 1
        else:
            print("You uncover a map with a red X marking the Sunken Ruins.")
            player["clues"] += 1

    elif location == "Sunken Ruins":
        print(
            "\nAncient stone pillars rise from the water as the ruins hum with energy."
        )
        print("1) Inspect the cracked statue")
        print("2) Open the chest under the water")
        print("3) Leave the ruins and continue")
        choice = get_choice({1: "Statue", 2: "Chest", 3: "Leave"})

        if choice == 1:
            print("A rune glows in your hand. You gain a clue to the final temple.")
            player["clues"] += 1
        elif choice == 2:
            print("The chest is trapped. A burst of water knocks you back.")
            player["health"] -= 2
        else:
            print(
                "You leave the ruins with a careful step and a growing sense of danger."
            )

    elif location == "Crystal Cave":
        print(
            "\nInside the cave, the walls sparkle with blue crystals and a low roar echoes ahead."
        )
        print("1) Take the crystal shard")
        print("2) Brave the narrow tunnel")
        print("3) Rest for a moment")
        choice = get_choice({1: "Shard", 2: "Tunnel", 3: "Rest"})

        if choice == 1:
            print(
                "The crystal shard shines brightly, granting you courage and 10 gold."
            )
            player["gold"] += 10
            player["health"] += 1
        elif choice == 2:
            print("You slip on a slick stone and lose a little health.")
            player["health"] -= 1
        else:
            print(
                "You rest, recover your strength, and prepare for the final challenge."
            )
            player["health"] += 1

    elif location == "Sky Temple":
        print(
            "\nThe temple doors open to an empty chamber with a gleaming treasure pedestal."
        )
        print("1) Claim the treasure")
        print("2) Read the ancient warning")
        print("3) Escape before the trap springs")
        choice = get_choice({1: "Treasure", 2: "Warning", 3: "Escape"})

        if choice == 1:
            print("You claim the treasure and become the island's winner.")
            player["gold"] += 30
            print("The temple lights flare and the island reveals its final secret.")
            return False
        elif choice == 2:
            print(
                "The warning tells you the island rewards courage and punishes greed."
            )
            player["clues"] += 1
        else:
            print("You escape with your life but leave the treasure behind.")
            player["gold"] += 5

    if player["health"] <= 0:
        print("\nYour health has reached zero. The island claims another explorer.")
        return False

    return True


def play_round(player):
    """Run a single full adventure path through the island.

    Args:
        player (dict): The current player state.

    Returns:
        None.
    """
    locations = [
        "Whispering Forest",
        "Sunken Ruins",
        "Crystal Cave",
        "Sky Temple",
    ]

    for location in locations:
        show_story(f"\nYou continue to the {location}...")
        if not handle_event(player, location):
            return

        print(f"\nHealth: {player['health']}")
        print(f"Gold: {player['gold']}")
        print(f"Clues: {player['clues']}")

        if location != "Sky Temple":
            next_step = input("\nDo you want to continue? (y/n): ").strip().lower()
            if next_step not in ["y", "yes"]:
                print("You decide to leave the island before the final challenge.")
                return

    print("\nYou have reached the end of the island and survived the journey.")
    print("Your final score is based on gold, clues, and health.")
    final_score = player["gold"] + (player["clues"] * 10) + player["health"] * 5
    print(f"Final score: {final_score}")

    if final_score >= 120:
        print("You win! The island honors your courage and treasure hunting skill.")
    elif final_score >= 80:
        print("You escape the island with a solid victory and a story to tell.")
    else:
        print("You survive, but the island keeps some of its secrets for later.")


def main():
    """Start the text-based game and loop until the player chooses to exit."""
    player_name = intro_game()
    player = {"health": 5, "gold": 0, "clues": 0, "name": player_name}

    while True:
        play_round(player)

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in ["y", "yes"]:
            print("Thanks for playing Moonlit Mystery!")
            break

        player = {"health": 5, "gold": 0, "clues": 0, "name": player_name}
        print("\nA new journey begins...\n")


if __name__ == "__main__":
    main()
