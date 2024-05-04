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
        if not (3 <= len(username) <= 25):
            return False
        elif username.startswith("-") or username.startswith("_"):
            return False
        elif username.endswith("-") or username.endswith("_"):
            return False
        elif not all(c.isalnum() or c in "-_" for c in username):
            return False

        r = Response(429)
        while r.status_code == 429:
            with httpx.Client(verify=False, proxies=self.proxies) as client:
                r = client.head(f"{self.ENDPOINT}{username}")
            if r.status_code == 429:
                time.sleep(self.RATELIMIT_TIMEOUT)
        
        return username if r.status_code == 404 else None