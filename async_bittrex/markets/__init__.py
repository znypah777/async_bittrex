
from async_bittrex.bases.factory import ProtectedSectionFactory
from async_bittrex.groups.protected_group import protected_group_factory


market_factory = ProtectedSectionFactory()


from .v1 import Market_v1_1

v1_1_endpoints = dict(BUY_LIMIT = "/market/buylimit",
                      SELL_LIMIT = "/market/selllimit",
                      CANCEL = "/market/cancel",
                      OPEN_ORDERS = "/market/getopenorders")

market_factory.register("v1.1", Market_v1_1, protected_group_factory.get_version("v1.1"), v1_1_endpoints)
