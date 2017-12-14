from async_bittrex.bases.factory import PublicSectionFactory
from async_bittrex.groups.public_group import public_group_factory



public_factory = PublicSectionFactory()

from .v1 import Public_v1_1, PublicV2_2

v1_1_endpoints = dict(MARKETS="/public/getmarkets",
                      CURRENCIES="/public/getcurrencies",
                      TICKER="/public/getticker",
                      MARKET_SUMMARIES="/public/getmarketsummaries",
                      MARKET_SUMMARY="/public/getmarketsummary",
                      ORDER_BOOK="/public/getorderbook",
                      MARKET_HISTORY ="/public/getmarkethistory")

v2_endpoints = dict(MARKETS="/public/getmarkets",
                    CURRENCIES="/public/getcurrencies",
                    TICKER="/public/getticker",
                    MARKET_SUMMARIES="/public/getmarketsummaries",
                    MARKET_SUMMARY="/public/getmarketsummary",
                    ORDER_BOOK="/public/getorderbook",
                    MARKET_HISTORY ="/public/getmarkethistory")


public_factory.register("v1.1", Public_v1_1, public_group_factory.get_version("v1.1"), v1_1_endpoints)
public_factory.register("v2.0", PublicV2_2, public_group_factory.get_version("v2.0"), v2_endpoints)