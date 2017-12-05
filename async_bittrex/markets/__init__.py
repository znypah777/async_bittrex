from async_bittrex.bases.factory import ProtectedSectionBaseFactory
from async_bittrex.groups.protected_group import protected_group_factory


market_factory = ProtectedSectionBaseFactory()


from .v1 import Market_v1_1

market_factory.register("v1.1", Market_v1_1, protected_group_factory.get_version("v1.1"))