"""https://soundcloud.com/
"""
import time

import httpx
from httpx._models import Response

from base.checker import BaseChecker


class Checker(BaseChecker):
    ENDPOINT = "https://steamcommunity.com/id/"

    @BaseChecker.check.register
    def _(self, username:str) -> str|None:
        if not (2 < len(username) <= 32):
            return None
        elif not all(c.isalnum() and c.isascii() or c in "-_" for c in username):
            return None

        r = Response(429)
        while r.status_code == 429:
            with httpx.Client(verify=False, proxies=self.proxies) as client:
                r = client.get(f"{self.ENDPOINT}{username}")
            if r.status_code == 429:
                time.sleep(self.RATELIMIT_TIMEOUT)
        
        return username if "The specified profile could not be found." in r.text else None