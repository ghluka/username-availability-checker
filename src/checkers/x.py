"""https://x.com/
"""
import httpx
from httpx._models import Response

from base.checker import BaseChecker


class Checker(BaseChecker):
    ENDPOINT = "https://api.twitter.com/i/users/username_available.json?username="

    @BaseChecker.check.register
    def _(self, username:str) -> bool:        
        r = Response(429)
        while r.status_code == 429:
            with httpx.Client(verify=False, proxies=self.proxies) as client:
                r = client.get(f"{self.ENDPOINT}{username}")
        
        return r.json()["valid"]