import pathlib
import time

from utils.checkers import get_checker, path
from utils.output import clear, title
from utils.prompts import select_checker, select_usernames


def main():
    clear()
    title()
    try:
        # Service selector
        checker_name = select_checker()
        print(f"\nSelected {checker_name.capitalize()}.")
        checker = get_checker(checker_name)

        # Username list selector
        usernames = select_usernames()
        print(f"\nSelected {len(usernames)} usernames from list.")

        # TODO: Prompt user for proxies and amount of threads

        # Get hits
        print("\nStarting...")
        start = time.perf_counter()
        hits = [r for r in checker.check(usernames)]
        elapsed = time.perf_counter() - start
        print(f"Done! Took {elapsed:.2f}s")

        # Save hits
        pathlib.Path(f"{path}/hits").mkdir(exist_ok=True)
        output_name = f"{checker_name.lower()}-{time.strftime('%Y%m%d-%H%M%S')}"
        with open(f"{path}/hits/{output_name}.txt", "w") as f:
            f.writelines("\n".join(hits))
    except (KeyboardInterrupt, EOFError):
        pass
    print("\nGoodbye!")


if __name__ == "__main__":
    main()