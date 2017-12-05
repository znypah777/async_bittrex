from bittrex.bases.group import BaseGroup as Base
from typing import Dict, Any, Optional

import hmac
import hashlib


class BaseGroup_v1_1(Base):
    def _gen_api_sig(self, endpoint: str) -> str:
        return hmac.new(self._api_secret.encode(),
                        endpoint.encode(),
                        hashlib.sha512).hexdigest()

    def _gen_internal_headers(self, **kwargs: Any) -> Dict[str, Any]:
        headers = {
            "apisign": self._gen_api_sig(kwargs.get("endpoint"))
        }
        return headers

    async def _get_query(self,
                         endpoint: str,
                         params: Optional[Dict[str, str]]=None,
                         extra_headers: Optional[Dict[str, str]]=None) -> Dict[str, str]:
        target = self._generate_url(endpoint,params=params)
        headers = self._gen_internal_headers(endpoint=target)
        if extra_headers is not None:
            headers.update(extra_headers)
        return await self._get(target, headers=headers)


