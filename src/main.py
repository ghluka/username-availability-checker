import pathlib
import time
import tkinter as tk
from tkinter import filedialog

from utils.checkers import get_checker, get_checkers, path
from utils.output import clear, print_columns

if __name__ == "__main__":
    try:
        # service selector
        clear()
        print("Checkers:")
        checkers = get_checkers()
        print_columns(checkers, start="  ", end="\n\n")

        name = input("Which checker do you want to use: ")
        while name.capitalize() not in checkers:
            print(" Invalid checker! Try again.\n")
            name = input("Which checker do you want to use: ")
        print(f"\nSelected {name.capitalize()}.\n")

        # TODO: Add selection for proxies, thread workers, etc...

        # username list selector
        root = tk.Tk()
        root.wm_attributes('-topmost', 1)
        root.withdraw()
        file = filedialog.askopenfilename(
            initialdir=f"{path}/presets",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not file:
            exit()
        with open(file) as f:
            usernames = f.read().splitlines()
        print(f"Selected \"{file}\".\n")

        # username checker
        checker = get_checker(name)

        print("Starting...\n")
        start = time.perf_counter()
        r = checker.check(usernames)
        
        hits = []
        for i, valid in enumerate(r):
            if valid:
                hits.append(usernames[i])
        
        # save hits
        elapsed = time.perf_counter() - start
        print(f"Done! Took {elapsed:.2f}s\n")

        pathlib.Path(f"{path}/hits").mkdir(exist_ok=True)
        with open(f"{path}/hits/hits-{time.strftime('%Y%m%d-%H%M%S')}.txt", "w") as f:
            f.writelines("\n".join(hits))
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")