"""https://soundcloud.com/
"""
import time

import httpx
from httpx._models import Response

from base.checker import BaseChecker


class Checker(BaseChecker):
    ENDPOINT = "https://soundcloud.com/"

    @BaseChecker.check.register
    def _(self, username:str) -> str|None:
        if not (3 < len(username) <= 25):
            return None
        elif username.startswith("-") or username.startswith("_"):
            return None
        elif username.endswith("-") or username.endswith("_"):
            return None
        elif not all(c.isalnum() and c.isascii() or c in "-_" for c in username):
            return None

        r = Response(429)
        while r.status_code == 429:
            with httpx.Client(verify=False, proxies=self.proxies) as client:
                r = client.head(f"{self.ENDPOINT}{username}")
            if r.status_code == 429:
                time.sleep(self.RATELIMIT_TIMEOUT)
        
        return username if r.status_code == 404 else None