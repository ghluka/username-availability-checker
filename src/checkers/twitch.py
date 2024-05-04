"""https://twitch.tv/
"""
import httpx
from httpx._models import Response

from base.checker import BaseChecker


class Checker(BaseChecker):
    ENDPOINT = "https://gql.twitch.tv/gql"

    @BaseChecker.check.register
    def _(self, username:str) -> bool:
        headers={'client-id': 'kimne78kx3ncx6brgo4mv6wki5h1ko'}
        payload = [{"operationName": "UsernameValidator_User", "variables": {"username": username}, "extensions": {"persistedQuery": {"version": 1, "sha256Hash": "fd1085cf8350e309b725cf8ca91cd90cac03909a3edeeedbd0872ac912f3d660"}}}]

        r = Response(429)
        while r.status_code == 429:
            with httpx.Client(verify=False, proxies=self.proxies) as client:
                r = client.post(self.ENDPOINT, headers=headers, json=payload)
        
        return r.json()[0]["data"]["isUsernameAvailable"]