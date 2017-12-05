

import aiohttp
import time

from async_bittrex.groups.base_group import basegroup_factory

class ProtectedGroup_v1_1(basegroup_factory.get_version("v1.1")):
    def __init__(self, session: aiohttp.ClientSession, api_key: str, api_secret: str, api_version: str):
        super().__init__(session, api_version)
        self._api_secret = api_secret
        self._api_key = api_key

    def _get_protected_params(self):
        return {
            "apikey": self._api_key,
            "nonce": str(int(time.time() * 1000))
        }

