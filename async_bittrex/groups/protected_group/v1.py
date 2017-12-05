
import time


from typing import Dict, Optional

class ProtectedGroup_v1_1:
    def __init__(self, api_key: str, group: object):
        self._api_key = api_key
        self._group = group

    def get_protected_params(self):
        return {
            "apikey": self._api_key,
            "nonce": str(int(time.time() * 1000))
        }

    async def get_query(self,
                         endpoint: str,
                         params: Optional[Dict[str, str]]=None,
                         extra_headers: Optional[Dict[str, str]]=None) -> Dict[str, str]:
        return await self._group.get_query(endpoint, params=params, extra_headers=extra_headers)