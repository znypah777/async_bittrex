
from typing import Optional, Dict

class PublicGroup_v1_1:
    def __init__(self, group: str):
        self._group = group

    async def get_query(self,
                         endpoint: str,
                         params: Optional[Dict[str, str]]=None,
                         extra_headers: Optional[Dict[str, str]]=None) -> Dict[str, str]:
        return await self._group.get_query(endpoint, params=params, extra_headers=extra_headers)