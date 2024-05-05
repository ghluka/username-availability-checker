import tkinter as tk
from tkinter import filedialog

from utils.checkers import get_checkers, path
from utils.output import print_columns

root = tk.Tk()
root.wm_attributes('-topmost', 1)
root.withdraw()


def select_checker() -> str:
    """Outputs list of checkers and prompts user to select one."""
    checkers = get_checkers()
    print(f"Checkers ({len(checkers)}):")
    print_columns(checkers, start="  ", end="\n")

    name = input("Which checker do you want to use: ")
    while name.capitalize() not in checkers:
        print(" Invalid checker! Try again.\n")
        name = input("Which checker do you want to use: ")
        
    return name


def select_usernames() -> str:
    """Opens file dialog and prompts for list of usernames. If cancelled, exits."""
    file = filedialog.askopenfilename(
        initialdir=f"{path}/presets",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not file:
        exit()
    
    with open(file) as f:
        usernames = f.read().splitlines()
        
    return usernames