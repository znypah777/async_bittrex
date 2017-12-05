import aiohttp

from typing import Dict, Any
from urllib.parse import urlencode


class BaseGroup:

    BASE_URL="https://bittrex.com/api"

    def __init__(self, session: aiohttp.ClientSession, api_version: str):
        self._session = session
        self._api_version = api_version

    def _generate_url(self, endpoint:str, params:Dict[str, str]=None) -> str:
        if params:
            return f"{BaseGroup.BASE_URL}/{self._api_version}{endpoint}?{urlencode(params)}"
        return f"{BaseGroup.BASE_URL}/{self._api_version}{endpoint}"

    async def _post(self, endpoint: str, data: Dict[str, str] = None, **extra: Dict[str, Any]) -> Dict[str, Any]:
        async with self._session.post(endpoint, data=data, **extra) as resp:
            return await resp.json()

    async def _get(self, endpoint: str, params: Dict[str, str] = None, **extra: Dict[str, Any]) -> Dict[str, Any]:
        async with self._session.get(endpoint, params=params, **extra) as resp:
            return await resp.json()


