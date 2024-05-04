import os


def clear() -> None:
    os.system("cls" if os.name == "nt" else "clear")

def print_columns(values:list, columns:int=3, start:str="", end:str="\n") -> None:
    out = start
    seperator = len(max(values, key=len))

    for i, value in enumerate(values, 1):
        out += f"{value: <{seperator}}"
        out += f"\n{start}" if i % columns == 0 else "    "
    
    print(out, end=end)