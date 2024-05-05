"""https://gitlab.com/
"""
import time

import httpx
from httpx._models import Response

from base.checker import BaseChecker


class Checker(BaseChecker):
    ENDPOINT = "https://gitlab.com/users/"

    @BaseChecker.check.register
    def _(self, username:str) -> str|None:
        r = Response(429)
        while r.status_code == 429:
            with httpx.Client(verify=False, proxies=self.proxies) as client:
                r = client.get(f"{self.ENDPOINT}{username}/exists")
            if r.status_code == 429:
                time.sleep(self.RATELIMIT_TIMEOUT)
        
        return username if r.json()['exists'] == False else None