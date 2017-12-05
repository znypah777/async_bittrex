import aiohttp

from typing import Dict, Any


class BaseGroup:

    def __init__(self, session: aiohttp.ClientSession):
        self._session = session

    async def _post(self, endpoint: str, data: Dict[str, str] = None, **extra: Dict[str, Any]) -> Dict[str, Any]:
        async with self._session.post(endpoint, data=data, **extra) as resp:
            return await resp.json()

    async def _get(self, endpoint: str, params: Dict[str, str] = None, **extra: Dict[str, Any]) -> Dict[str, Any]:
        async with self._session.get(endpoint, params=params, **extra) as resp:
            return await resp.json()