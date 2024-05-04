import concurrent.futures
from functools import singledispatchmethod

from httpx._types import ProxiesTypes

class BaseChecker:
    ENDPOINT = ""

    def __init__(self, proxies:ProxiesTypes=None, max_workers:int=5) -> None:
        self.proxies = proxies
        self.max_workers = max_workers

    @singledispatchmethod
    def check(self, username) -> bool:
        """Checks if username is available"""
        raise NotImplementedError
    
    @check.register
    def _(self, usernames:list) -> list[bool]:
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {executor.submit(self.check, username): username for username in usernames}
            r = []
            for future in concurrent.futures.as_completed(futures):
                r.append(future.result())

        return r