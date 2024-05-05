import os


def clear() -> None:
    """Clears screen"""
    os.system("cls" if os.name == "nt" else "clear")


def title() -> None:
    """Outputs title as ASCII art"""
    print(
        "  ██    ██  █████   ██████ \n" \
        "  ██    ██ ██   ██ ██      \n" \
        "  ██    ██ ███████ ██      \n" \
        "  ██    ██ ██   ██ ██      \n" \
        "   ██████  ██   ██  ██████ \n" \
        "Username Availability Checker" + "\n"
    )


def print_columns(values:list, columns:int=3, start:str="", end:str="\n") -> None:
    """Outputs list in columns"""
    out = start
    seperator = len(max(values, key=len))

    for i, value in enumerate(values, 1):
        out += f"{value: <{seperator}}"
        out += f"\n{start}" if i % columns == 0 else "    "
    
    print(out, end=end)