"""https://chess.com/
"""
import time

import httpx
from httpx._models import Response

from base.checker import BaseChecker


class Checker(BaseChecker):
    ENDPOINT = "https://www.chess.com/callback/user/valid?username="

    @BaseChecker.check.register
    def _(self, username:str) -> str|None:        
        r = Response(429)
        while r.status_code == 429:
            with httpx.Client(verify=False, proxies=self.proxies) as client:
                r = client.get(f"{self.ENDPOINT}{username}")
            if r.status_code == 429:
                time.sleep(self.RATELIMIT_TIMEOUT)
        
        print(r.json(), username)
        return username if r.json()["valid"] else None