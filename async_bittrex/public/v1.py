
from typing import Dict, List, Optional
from datetime import datetime

class Public_v1_1:

    def __init__(self, group, endpoints):
        self._group = group
        self._endpoints = endpoints

    async def get_markets(self, extra_headers: Optional[Dict[str, str]]=None):
        return await self._group.get_query(self._endpoints["MARKETS"], extra_headers=extra_headers)

    async def get_currencies(self, extra_headers: Optional[Dict[str, str]]=None):
        return await self._group.get_query(self._endpoints["CURRENCIES"], extra_headers=extra_headers)

    async def get_ticker(self, market:str, extra_headers: Optional[Dict[str, str]]=None):
        resp = await self._group.get_query(self._endpoints["TICKER"], params={"market": market}, extra_headers=extra_headers)
        resp["market"] = market
        return resp

    async def get_market_summaries(self, extra_headers: Optional[Dict[str, str]]=None) -> Dict[str,str]:
        return await self._group.get_query(self._endpoints["MARKET_SUMMARIES"], extra_headers=extra_headers)

    async def get_market_summary(self, market: str, extra_headers: Optional[Dict[str, str]]=None) -> Dict[str, str]:
        return await self._group.get_query(self._endpoints["MARKET_SUMMARY"], params={"market": market}, extra_headers=extra_headers)

    async def get_orderbook(self, market: str, orderbook_type:str, extra_headers: Optional[Dict[str, str]]=None):
        response = await self._group.get_query(self._endpoints["MARKET_SUMMARY"],
                                               params={"market": market, "type": orderbook_type},
                                               extra_headers=extra_headers)

        response["market"] = market
        return response

    async def get_market_history(self, market: str, extra_headers: Optional[Dict[str, str]]=None):
        response = await self._group.get_query(self._endpoints["MARKET_HISTORY"],
                                               params={"market": market},
                                               extra_headers=extra_headers)
        response["market"] = market
        return response



class PublicV2_2(Public_v1_1):
    async def get_ticker(self, market:str, interval:str, extra_headers: Optional[Dict[str, str]]=None):
        timestamp = datetime.now().strftime("%s")
        return await self._group.get_query(self._endpoints["LATEST_TICK"],
                                           params={"marketName": market,
                                                   "tickInterval": interval,
                                                   "_": timestamp})

    async def get_ticks(self, market:str, interval:str, extra_headers: Optional[Dict[str, str]]=None):
        timestamp = datetime.now().strftime("%s")
        return await self._group.get_query(self._endpoint["TICKS"], params={"marketName": market,
                                                                      "tickInterval": interval,
                                                                      "_": timestamp})