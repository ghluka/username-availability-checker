if __name__ == "__main__":
    # TODO: Add proper menu where you can select proxies, thread workers, etc...
    checker = __import__("checkers.speedrun-com", fromlist=[None]).Checker()
    r = checker.check(input("Enter a username to check: "))
    if r:
        print("Available!")
    else:
        print("Unavailable.")