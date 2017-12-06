import asyncio


from typing import Dict, Any, List, Optional


class Market_v1_1:

    BUY_LIMIT = "/market/buylimit"
    SELL_LIMIT = "/market/selllimit"
    CANCEL = "/market/cancel"
    OPEN_ORDERS = "/market/getopenorders"
    
    def __init__(self, group):
        self._group = group
    
    async def buy_limit(self,
                        market: str,
                        quantity: float,
                        rate: float,
                        extra_headers: Optional[Dict[str, str]]=None) -> Dict[str, Any]:
        params = {"market": market,
                  "quantity": quantity,
                  "rate": rate,
                  **self._group.get_protected_params()}
        response = await self._group.get_query(Market_v1_1.BUY_LIMIT, params=params, extra_headers=extra_headers)
        response["market"] = market
        return response

    async def buy_limits(self, buy_data: List[Dict[str, Any]], extra_headers: Optional[Dict[str, str]]=None) -> List[Dict[str, Any]]:
        tasks = []
        for data in buy_data:
            tasks.append(self.buy_limit(data["market"],
                                        data["quantity"],
                                        data["rate"],
                                        extra_headers=extra_headers))
        return await asyncio.gather(*tasks)
    
    async def sell_limit(self,
                         market: str,
                         quantity: float,
                         rate: float,
                         extra_headers: Optional[Dict[str, str]]=None) -> Dict[str, Any]:
        params = {"market": market,
                  "quantity": quantity,
                  "rate": rate,
                  **self._group.get_protected_params()}
        response = await self._group.get_query(Market_v1_1.SELL_LIMIT, params=params, extra_headers=extra_headers)
        response["market"] = market
        return response
    
    async def sell_limits(self, market_data: List[str], extra_headers: Optional[Dict[str, str]]=None) -> List[Dict[str, Any]]:
        tasks = []
        for data in market_data:
            tasks.append(self.sell_limit(data["market"],
                                        data["quantity"],
                                        data["rate"],
                                        extra_headers=extra_headers))
        return await asyncio.gather(*tasks)

    async def cancel(self, uuid: str, extra_headers: Optional[Dict[str, str]]=None) -> Dict[str,Any]:
        response = await self._group.get_query(Market_v1_1.CANCEL,
                                               params={"uuid":uuid,
                                             **self._group.get_protected_params()},
                                               extra_headers=extra_headers)
        response["order_id"] = uuid
        return response

    async def cancel_many(self, uuids: List[str], extra_headers: Optional[Dict[str, str]]=None) -> List[Dict[str, Any]]:
        return await self._group.get_multiple(uuids, self.get_open_orders, extra_headers=extra_headers)

    async def get_open_orders(self, market: Optional[str] = None, extra_headers: Optional[Dict[str, str]]=None) -> Dict[str, Any]:
        params = self._group.get_protected_params()
        if market is not None:
            params["market"] = market
        response  = await self._group.get_query(Market_v1_1.OPEN_ORDERS, params=params, extra_headers=extra_headers)
        response["market"] = market
        return response

    async def get_open_orders_for(self, markets: List[str], extra_headers: Optional[Dict[str, str]]=None) -> List[Dict[str, Any]]:
        return await self._group.get_multiple(markets, self.get_open_orders, extra_headers=extra_headers)