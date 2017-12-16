import asyncio


from typing import Dict, Any, List, Optional


class Market_v1_1:
    """
      Market section of Bittrex API as of v1.1

      contains all the methods the Market section has
    """

    def __init__(self, group:object, endpoints: Dict[str, str]):
        self._group = group
        self._endpoints = endpoints

    async def buy_limit(self,
                        market: str,
                        quantity: float,
                        rate: float,

                        extra_headers: Optional[Dict[str, str]]=None) -> Dict[str, Any]:
        params = {"market": market,
                  "quantity": quantity,
                  "rate": rate,
                  **self._group.get_protected_params()}
        response = await self._group.get_query(self._endpoints["BUY_LIMIT"], params=params, extra_headers=extra_headers)
        response["market"] = market
        return response

    async def sell_limit(self,
                         market: str,
                         quantity: float,
                         rate: float,
                         extra_headers: Optional[Dict[str, str]]=None) -> Dict[str, Any]:
        params = {"market": market,
                  "quantity": quantity,
                  "rate": rate,
                  **self._group.get_protected_params()}

        response = await self._group.get_query(self._endpoints["SELL_LIMIT"], params=params, extra_headers=extra_headers)
        response["market"] = market
        return response

    async def cancel(self, uuid: str, extra_headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        response = await self._group.get_query(self._endpoints["CANCEL"],
                                               params={"uuid": uuid,
                                                       **self._group.get_protected_params()},
                                               extra_headers=extra_headers)
        response["order_id"] = uuid
        return response

    async def get_open_orders(self,
                              market: Optional[str] = None,
                              extra_headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        params = self._group.get_protected_params()
        if market is not None:
            params["market"] = market
        response = await self._group.get_query(self._endpoints["OPEN_ORDERS"], params=params, extra_headers=extra_headers)
        response["market"] = market
        return response

