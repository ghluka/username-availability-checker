"""https://github.com/
"""
import time

import httpx
from httpx._models import Response

from base.checker import BaseChecker


class Checker(BaseChecker):
    ENDPOINT = "https://github.com/"

    @BaseChecker.check.register
    def _(self, username:str) -> str|None:
        if len(username) > 39:
            return False
        elif username.endswith("-") or username.endswith("-") or "--" in username:
            return False
        elif not all(c.isalnum() and c.isascii() or c in "-" for c in username):
            return False
        
        r = Response(429)
        while r.status_code == 429:
            with httpx.Client(verify=False, proxies=self.proxies) as client:
                r = client.get(f"{self.ENDPOINT}{username}")
            if r.status_code == 429:
                time.sleep(self.RATELIMIT_TIMEOUT)
        
        return username if r.status_code == 404 else None