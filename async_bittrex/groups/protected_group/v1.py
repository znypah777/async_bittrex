
import time


from typing import Dict, Optional, Callable, Awaitable, Any, List

class ProtectedGroup_v1_1:
    """
        This class is for the protected sections of the Bittrex API namely the Accounts ans Markets Section
    """
    def __init__(self, api_key: str, group: object):
        self._api_key = api_key
        self._group = group

    def get_protected_params(self):
        """
            creates the extra needed params for the protected sections
        """
        return {
            "apikey": self._api_key,
            "nonce": str(int(time.time() * 1000))
        }

    async def get_query(self,
                         endpoint: str,
                         params: Optional[Dict[str, str]]=None,
                         extra_headers: Optional[Dict[str, str]]=None) -> Dict[str, str]:
        """
            Wrapper for the basegroup get_query method to avoid feature envy
        """
        return await self._group.get_query(endpoint, params=params, extra_headers=extra_headers)

    async def get_multiple(self,
                           items: List[str],
                           call_back: Callable[[str], Awaitable[List[Dict[str, str]]]],
                           extra_headers: Optional[Dict[str, Any]] = None) -> List[Dict[str, str]]:
        """
            Wrapper for the basegroup get_multiple method to avoid feature envy
        """

        return await self._group.get_multiple(items, call_back, extra_headers=extra_headers)