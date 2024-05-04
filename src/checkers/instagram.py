"""https://instagram.com/
"""
import httpx
from httpx._models import Response

from base.checker import BaseChecker


class Checker(BaseChecker):
    ENDPOINT = "https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/"

    @BaseChecker.check.register
    def _(self, username:str) -> bool:
        headers = {'X-CSRFToken': 'en'}
        payload = {'email': '', 'username': username, 'first_name': '', 'opt_into_one_tap': False}
        
        r = Response(429)
        while r.status_code == 429:
            with httpx.Client(verify=False, proxies=self.proxies) as client:
                r = client.post(self.ENDPOINT, data=payload, headers=headers)
        
        return not '"username": [{"message": ' in r.text