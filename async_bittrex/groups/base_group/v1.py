from async_bittrex.bases.group import BaseGroup as Base
from typing import Dict, Any, Optional
from urllib.parse import urlencode

import hmac
import hashlib
import aiohttp


class BaseGroup_v1_1(Base):
    BASE_URL = "https://bittrex.com/api"

    def __init__(self, session: aiohttp.ClientSession, api_secret:str, api_version: str):
        super().__init__(session)
        self._api_secret = api_secret
        self._api_version = api_version


    def _generate_url(self, endpoint:str, params:Dict[str, str]=None) -> str:
        if params:
            return f"{BaseGroup_v1_1.BASE_URL}/{self._api_version}{endpoint}?{urlencode(params)}"
        return f"{BaseGroup_v1_1.BASE_URL}/{self._api_version}{endpoint}"

    def _gen_api_sig(self, endpoint: str) -> str:
        return hmac.new(self._api_secret.encode(),
                        endpoint.encode(),
                        hashlib.sha512).hexdigest()

    async def get_query(self,
                         endpoint: str,
                         params: Optional[Dict[str, str]]=None,
                         extra_headers: Optional[Dict[str, str]]=None) -> Dict[str, str]:
        target = self._generate_url(endpoint,params=params)
        api_sig = self._gen_api_sig(target)
        headers = {"apisign": api_sig}
        if extra_headers is not None:
            headers.update(extra_headers)
        return await self._get(target, headers=headers)
