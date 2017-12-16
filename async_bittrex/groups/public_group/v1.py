
from typing import Optional, Dict, List, Callable, Awaitable, Any

class PublicGroup_v1_1:
    """
        This class is for the non protected parts of the API
        the parts that don't need an API key as of Bittrex API v1.1 there is only one section that is public
        and that is called the Public section
    """
    def __init__(self, group: str):
        self._group = group

    async def get_query(self,
                         endpoint: str,
                         params: Optional[Dict[str, str]]=None,
                         extra_headers: Optional[Dict[str, str]]=None) -> Dict[str, str]:
        """
            Wrapper for the basegroup get_query method to avoid feature envy
        """

        return await self._group.get_query(endpoint, params=params, extra_headers=extra_headers)