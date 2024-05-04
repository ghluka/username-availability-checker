import utils.checkers
from utils.output import print_columns

if __name__ == "__main__":
    try:
        # service selector
        print("Checkers:")
        checkers = utils.checkers.get_checkers()
        print_columns(checkers, start="  ", end="\n\n")

        name = input("Which checker do you want to use: ")
        while name not in checkers:
            print(" Invalid checker! Try again.\n")
            name = input("Which checker do you want to use: ")
        print()

        # TODO: Add selection for proxies, thread workers, etc...

        # username checker
        # TODO: Allow user to select from file, output valids in another file
        checker = utils.checkers.get_checker(name)
        r = checker.check(input("Enter a username to check: "))
        if r:
            print(" Available!")
        else:
            print(" Unavailable.")
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")