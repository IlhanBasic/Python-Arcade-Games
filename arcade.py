import sys
from rps import rps
from guess_number import guess_number
from zigzag import zig_zag_game
from snake import snake_game
def play_game(name='PlayerOne'):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu.")

        playerchoice = input(
            "\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n3 = Zigzag game\n4 = Snake\n\nOr press \"x\" to exit the Arcade\n\n"
        )

        if playerchoice not in ["1", "2","3","4", "x"]:
            print(f"\n{name}, please enter 1, 2, 3 or x.")
            return play_game(name)

        welcome_back = True

        if playerchoice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerchoice == "2":
            guess_my_number = guess_number(name)
            guess_my_number()
        elif playerchoice == "3":
            zig_zag = zig_zag_game(name)
            zig_zag()
        elif playerchoice == "4":
            snake = snake_game()
            snake()
        else:
            print("\nSee you next time!\n")
            sys.exit(f"Bye {name}! 👋")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        '-n', '--name', metavar='name',
        required=True, help='The name of the person playing the game.'
    )

    args = parser.parse_args()

    print(f"\n{args.name}, welcome to the Arcade! 🤖")

    play_game(args.name)
