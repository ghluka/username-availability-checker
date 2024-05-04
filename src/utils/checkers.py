import pathlib

from base.checker import BaseChecker


def get_checkers() -> list[str]:
    path = pathlib.Path(__file__).parent.parent.resolve()
    checkers = [
        checker.resolve().as_posix().split("/")[-1].removesuffix(".py").replace("-", ".")
        for checker in path.glob("checkers/*.py")
    ]

    return checkers

def get_checker(name:str) -> BaseChecker:
    module = __import__(f"checkers.{name.replace('.', '-')}", fromlist=[None])
    checker = module.Checker()

    return checker