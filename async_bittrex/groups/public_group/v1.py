import aiohttp

from async_bittrex.groups.base_group import basegroup_factory


class PublicGroup_v1_1(basegroup_factory.get_version("v1.1")):
    def __init__(self, session: aiohttp.ClientSession, api_secret: str, api_version: str):
        super().__init__(session, api_version)
        self._api_secret = api_secret

