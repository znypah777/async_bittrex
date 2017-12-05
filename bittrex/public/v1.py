

import asyncio
from typing import Dict, List, Optional
from bittrex.groups.public_group import public_group_factory

class Public_v1_1(public_group_factory.get_version("v1.1")):
    MARKETS = "/public/getmarkets"
    CURRENCIES = "/public/getcurrencies"
    TICKER = "/public/getticker"
    MARKET_SUMMARIES = "/public/getmarketsummaries"
    MARKET_SUMMARY = "/public/getmarketsummary"
    ORDER_BOOK = "/public/getorderbook"
    MARKET_HISTORY  = "/public/getmarkethistory"

    async def get_markets(self, extra_headers: Optional[Dict[str, str]]=None):
        return await self._get_query(Public_v1_1.MARKETS, extra_headers=extra_headers)

    async def get_currencies(self, extra_headers: Optional[Dict[str, str]]=None):
        return await self._get_query(Public_v1_1.CURRENCIES, extra_headers=extra_headers)

    async def get_ticker(self, market:str, extra_headers: Optional[Dict[str, str]]=None):
        resp = await self._get_query(Public_v1_1.TICKER, params={"market": market}, extra_headers=extra_headers)
        resp["market"] = market
        return resp

    async def get_tickers(self, markets: List[str], extra_headers: Optional[Dict[str, str]]=None):
        tasks = []
        for market in markets:
            tasks.append(self.get_ticker(market, extra_headers=extra_headers))
        return await asyncio.gather(*tasks)

    async def get_market_summaries(self, extra_headers: Optional[Dict[str, str]]=None):
        return await self._get_query(Public_v1_1.MARKET_SUMMARIES, extra_headers=extra_headers)

    async def get_market_summary(self, market: str, extra_headers: Optional[Dict[str, str]]=None):
        return await self._get_query(Public_v1_1.MARKET_SUMMARY, params={"market": market}, extra_headers=extra_headers)

    async def get_orderbook(self, market: str, orderbook_type:str, extra_headers: Optional[Dict[str, str]]=None):
        response = await self._get_query(Public_v1_1.MARKET_SUMMARY,
                                     params={"market": market, "type": orderbook_type},
                                     extra_headers=extra_headers)
        response["market"] = market
        return response

    async def get_market_history(self, market: str, extra_headers: Optional[Dict[str, str]]=None):
        response = await self._get_query(Public_v1_1.MARKET_HISTORY,
                                         params={"market": market},
                                         extra_headers=extra_headers)
        response["market"] = market
        return response

    async def get_market_histories(self, markets: List[str],  extra_headers: Optional[Dict[str, str]]=None):
        tasks = []
        for market in markets:
            tasks.append(self.get_market_history(market, extra_headers))
        return await asyncio.gather(*tasks)