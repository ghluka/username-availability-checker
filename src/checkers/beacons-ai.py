"""https://beacons.ai/
"""
import time

import httpx
from httpx._models import Response

from base.checker import BaseChecker


class Checker(BaseChecker):
    ENDPOINT = "https://account.beacons.ai/api/user_profile"

    @BaseChecker.check.register
    def _(self, username:str) -> str|None:
        if len(username) > 30:
            return None
        elif username.startswith(".") or username.endswith(".") or ".." in username:
            return None
        elif "__" in username:
            return None
        elif not all(c.isalnum() and c.isascii() or c in "_." for c in username):
            return None
        
        headers = {"X-Beacons-Application-Viewed": "web", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"}
        payload = {"new_username": username, "action": "is_username_taken"}

        r = Response(429)
        while r.status_code == 429:
            with httpx.Client(verify=False, proxies=self.proxies) as client:
                r = client.post(self.ENDPOINT, json=payload, headers=headers)
            if r.status_code == 429:
                time.sleep(self.RATELIMIT_TIMEOUT)
        
        return username if r.json()["username_taken"] == False else None