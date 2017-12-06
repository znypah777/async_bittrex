import asyncio

from typing import List, Dict, Any, Optional



class Account_v1_1:
    BALANCE = "/account/getbalance"
    DEPOSIT_ADDRESS = "/account/getdepositaddress"
    WITHDRAW = "/account/withdraw"
    ORDER = "/account/getorder"
    ORDER_HISTORY = "/account/getorderhistory"
    WITHDRAWAL_HISTORY = "/account/getwithdrawalhistory"
    DEPOSIT_HISTORY = "/account/getdeposithistory"
    
    def __init__(self, group: object):
        self._group = group

    async def get_balance(self, currency: str, extra_headers: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        params = {
            "currency": currency,
            **self._group.get_protected_params()
        }
        return await self._group.get_query(Account_v1_1.BALANCE, params=params, extra_headers=extra_headers)

    async def get_balances(self,
                           currencies: List[str],
                           extra_headers: Optional[Dict[str, str]] = None) -> List[Dict[str, str]]:
        return await self._group.get_multiple(currencies, self.get_balance, extra_headers=extra_headers)

    async def get_deposit_address(self, currency, extra_headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        return await self._group.get_query(Account_v1_1.DEPOSIT_ADDRESS,
                                           params={"currency": currency,
                                             **self._group.get_protected_params()},
                                           extra_headers=extra_headers)

    async def get_deposit_addresses(self,
                                    currencies: List[str],
                                    extra_headers: Optional[Dict[str, str]] = None) -> List[Dict[str, Any]]:
        return await self._group.get_multiple(currencies, self.get_deposit_address, extra_headers=extra_headers)


    async def withdraw(self, currency: str,
                       quantity: int,
                       address: str,
                       payment_id: Optional[int] = None,
                       extra_headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        params = {"currency": currency,
                  "quantity": quantity,
                  "address": address,
                  **self._group.get_protected_params()}

        if payment_id is not None:
            params["paymentid"] = payment_id

        response = await self._group.get_query(Account_v1_1.WITHDRAW, params=params, extra_headers=extra_headers)
        response["currency"] = currency
        return response

    async def withdraw_multiple(self,
                                currency_infos: List[Dict[str, str]],
                                extra_headers: Optional[Dict[str, str]] = None) -> List[Dict[str, Any]]:
        tasks = []
        for currency_info in currency_infos:
            tasks.append(self.withdraw(currency_info["currency"],
                                       currency_info["quantity"],
                                       currency_info["address"],
                                       currency_info.get("paymentid"),
                                       extra_headers=extra_headers))
        return await asyncio.gather(*tasks)

    async def get_order(self, uuid: str, extra_headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        return await self._group.get_query(Account_v1_1.ORDER, params={"uuid": uuid}, extra_headers=extra_headers)

    async def get_orders(self, uuids: List[str], extra_headers: Optional[Dict[str, str]] = None) -> List[Dict[str, Any]]:
        return self._group.get_multiple(uuids, self.get_order, extra_headers=extra_headers)

    async def get_order_history(self,
                                market: Optional[str] = None,
                                extra_headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        params = self._group.get_protected_params()
        if market is not None:
            params["market"] = market
        response = await self._group.get_query(Account_v1_1.ORDER_HISTORY, params=params, extra_headers=extra_headers)
        if market is not None:
            response["market"] = market
        return response

    async def get_order_histories(self,
                                  markets: List[str],
                                  extra_headers: Optional[Dict[str, str]] = None) -> List[Dict[str, Any]]:

        return await self._group.get_multiple(markets, self.get_order_history, extra_headers=extra_headers)

    async def get_withdrawal_history(self, market: Optional[str] = None,
                                     extra_headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        params = self._group.get_protected_params()
        if market is not None:
            params["market"] = market
        response = await self._group.get_query(Account_v1_1.WITHDRAWAL_HISTORY, params=params, extra_headers=extra_headers)
        if market is not None:
            response["market"] = market
        return response

    async def get_withdrawal_histories(self,
                                       markets: List[str],
                                       extra_headers: Optional[Dict[str, str]] = None) -> List[Dict[str, Any]]:
        return await self._group.get_multiple(markets, self.get_withdrawal_history, extra_headers=extra_headers)

    async def get_deposit_history(self,
                                  market: Optional[str] = None,
                                  extra_headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        params = self._group.get_protected_params()
        if market is not None:
            params["market"] = market
        response = await self._group.get_query(Account_v1_1.DEPOSIT_HISTORY, params=params, extra_headers=extra_headers)
        if market is not None:
            response["market"] = market
        return response

    async def get_deposit_histories(self,
                                    markets: List[str],
                                    extra_headers: Optional[Dict[str, str]] = None) -> List[Dict[str, Any]]:

        return await self._group.get_multiple(markets, self.get_deposit_history, extra_headers=extra_headers)

