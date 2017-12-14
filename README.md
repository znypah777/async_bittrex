Async Bittrex

Asychronous Bittrex API wrapper

Supports all the current bittrex API endpoints as of v1.1 as well as other helper methods for batched queries like the example below

Example:

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
  
    
            print("market open orders")
            pprint(await market.get_open_orders_for(["BTC-LTC", "BTC-ADA",  "BTC-BCC", "BTC-BAY", "BTC-GBYTE"]))
            print("\n\n\n\n")
    
            print("public tickers")
            pprint(await public.get_tickers(["BTC-LTC", "BTC-ADA", "BTC-BCC", "BTC-BAY", "BTC-GBYTE"]))
            print("\n\n\n\n")
    
            print("account order histories")
            pprint(await accounts.get_order_histories(["BTC-LTC", "BTC-ADA", "BTC-BCC", "BTC-BAY", "BTC-GBYTE"]))
            print("\n\n\n\n")
    
    
    if __name__ == "__main__":
        loop = asyncio.get_event_loop()
        loop.run_until_complete(start())
        loop.close()


Output:

    market open orders
    [{'market': 'BTC-LTC', 'message': '', 'result': [], 'success': True},
     {'market': 'BTC-ADA', 'message': '', 'result': [], 'success': True},
     {'market': 'BTC-BCC', 'message': '', 'result': [], 'success': True},
     {'market': 'BTC-BAY', 'message': '', 'result': [], 'success': True},
     {'market': 'BTC-GBYTE', 'message': '', 'result': [], 'success': True}]
    
    public tickers
    [{'market': 'BTC-LTC',
      'message': '',
      'result': {'Ask': 0.00869102, 'Bid': 0.00868647, 'Last': 0.00869102},
      'success': True},
     {'market': 'BTC-ADA',
      'message': '',
      'result': {'Ask': 1.127e-05, 'Bid': 1.126e-05, 'Last': 1.126e-05},
      'success': True},
     {'market': 'BTC-BCC',
      'message': '',
      'result': {'Ask': 0.1299, 'Bid': 0.12974491, 'Last': 0.12974491},
      'success': True},
     {'market': 'BTC-BAY',
      'message': '',
      'result': {'Ask': 6.98e-06, 'Bid': 6.91e-06, 'Last': 6.91e-06},
      'success': True},
     {'market': 'BTC-GBYTE',
      'message': '',
      'result': {'Ask': 0.02529001, 'Bid': 0.02521187, 'Last': 0.02521187},
      'success': True}]
    
    account order histories
    [{'market': 'BTC-LTC', 'message': '', 'result': [], 'success': True},
     {'market': 'BTC-ADA', 'message': '', 'result': [], 'success': True},
     {'market': 'BTC-BCC', 'message': '', 'result': [], 'success': True},
     {'market': 'BTC-BAY', 'message': '', 'result': [], 'success': True},
     {'market': 'BTC-GBYTE', 'message': '', 'result': [], 'success': True}]


Disclaimer:
This only works with python3.6