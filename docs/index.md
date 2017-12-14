There are 3 factories that you must use:

 1. market_factory: for market related endpoints
 2. account_factory: for account related endpoints
 3. public_factory: for public related endpoints


How to initialize the factories:

 

    from bittrex.accounts import account_factory
    from bittrex.public import public_factory
    from bittrex.markets import market_factory
    from pprint import pprint
    import asyncio
    import aiohttp
    
    
    async def start():
        async with aiohttp.ClientSession() as session:
            market = market_factory(session, "your_api_key", "your_secret","v1.1")
            public = public_factory(session,  "your_secret","v1.1")
            accounts = account_factory(session, "your_api_key", "your_secret","v1.1")
               
         
    if __name__ == "__main__":
        loop = asyncio.get_event_loop()
        loop.run_until_complete(start())
        loop.close()


from this point forward we will now refer to the initialized factories as such:

 1. market: for the market_factory
 2. account: for the account factory
 3. public for the public factory


----------





    

> #MARKETS


_**market.buy_limit**_

`response = await market.buy_limit("BTC",  4.0, 4.0)`

_**market.buy_limits**_

`response = await market.buy_limit([{"currency": "BTC",  "rate": 4.0, "quantity:" 4.0], {"currency": "ADA", "rate": 5.0, "quantity": 4.0})`

_**market.sell_limit**_

`response = await market.sell_limit("BTC",  4.0, 4.0)`



_**market.sell_limits**_

`response = await market.sell_limits([{"currency": "BTC",  "rate": 4.0, "quantity:" 4.0], {"currency": "ADA", "rate": 5.0, "quantity": 4.0})`


_**market.cancel**_

`response = await market.cancel("some_uuid")`

_**market.cancel_many**_

`response = await market.cancel(["some_uuid1", "some_uuid2", "some_uuid3"])`

_**market.get_open_orders**_

    \\returns all open orders 
    response = await market.get_open_orders()
    
    \\returns order from specific market
    response = await market.get_open_orders("BTC")


_**market.get_open_orders_for**_

    \\returns all open orders for specified markets 
    response = await market.get_open_orders_for(["BTC-ETH", "BTC-ADA"])


----------


> #Accounts

_**account.get_balance**_

`response = await account.get_balance("BTC")`

_**account.get_balances**_

`response = await account.get_balances(["BTC", "ADA", "IOT"])`

_**account.get_deposit_address**_

`response = await account.get_deposit_address("BTC")`

_**account.get_deposit_addresses**_

`response = await account.get_deposit_addresses(["BTC", "ADA", "IOT"])`

_**account.withdraw**_

    \\ takes a curreny: str
               quantity: int
               address: str,
               payment_id: Optional[str]
               
    response = await account.withdraw("BTC", 10, "your btc address")

_**account.withdraw_multiple**_

    
      items = [
        {
            "currency": "BTC",
             "quantity": 4,
             "address": "btc_address"
        },
        {
            "currency": "ADA",
            "quantity": 4,
            "address": "btc_address"
        }
    ]
    \\ takes a list of dictionaries
      response = await account.withdraw_multiple(items)

_**account.get_order**_

`response = await account.get_order("some_uuid"))`
  
_**account.get_orders**_

`response = await account.get_orders(["uuid1", "uuid2", "uuid3"])`
  
_**account.get_order_history**_
 

     //get all order history from all avaliable markets
      response = await account.get_order_history()
      
    //get order history from one specific market
    response = await account.get_order_history("BTC-ADA")

_**account.get_order_histories**_

    // get multiple order histories from specified markets
     response = await account.get_order_history(["BTC-ADA", "BTC-ETH", "BTC-IOT"])


_**account.get_withdrawal_history**_
 

     //get all withdrawal history from all avaliable markets
      response = await account.get_withdrawal_history()
      
    //get withdrawal history from one specific market
    response = await account.get_withdrawal_history("BTC-ADA")


_**account.get_withdrawal_histories**_

    // get multiple withdrawal histories from specified markets
     response = await account.get_withdrawal_histories(["BTC-ADA", "BTC-ETH", "BTC-IOT"])
  

_**account.get_deposit_history**_
 

     //get all deposit history from all avaliable markets
      response = await account.get_deposit_history()
      
    //get deposit history from one specific market
    response = await account.get_deposit_history("BTC-ADA")

_**account.get_deposit_histories**_

    // get multiple withdrawal histories from specified markets
     response = await account.get_deposit_histories(["BTC-ADA", "BTC-ETH", "BTC-IOT"])


----------

> #Public

_**public.get_markets**_

`response = await public.get_markets()`

_**public.get_currencies**_

`response = await public.get_currencies()`

_**public.get_ticker**_

    // takes a market: str to get a ticker of
    market = ["BTC""] 
    `response = await public.get_ticker(market)`

_**public.get_tickers**_

    //takes list of markets to get tickers of
    markets = ["BTC", "ADA", "IOT"]
    response = await public.get_tickers(markets)


_**public.get_market_summary**_

    //takes a market to get a summary of
    market = "BTC"
    response = await public.get_market_summary(market)
    
_**public.get_market_summaries**_

    //takes all summaries of the marke. takes no arguments
    response = await public.get_market_summaries()
 

**_public.get_market_summary_for_**

    //takes all summaries of specified markets
    markets = ["BTC", "ADA", "IOT"]
    response = await public.get_market_summaries_for(markets)

_**public.get_orderbook**_

    //takes a market to get an order book of
    market = "BTC"
    response = await public.get_orderbook(market)

_**public.get_orderbooks**_

    //takes a list of markets to get an orders book of
    markets = ["BTC", "ADA", "IOT"]
    response = await public.get_orderbooks(market)

_**public.get_market_history**_
  
     //takes a markets to get a history of
        market = "BTC",
        response = await public.get_market_history(market)

_**public.get_market_histories**_

    //takes a list of markets to get histories of
    markets = ["BTC", "ADA", "IOT"]
    response = await public.get_market_histories(markets)








