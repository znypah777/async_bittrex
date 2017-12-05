from async_bittrex.bases.factory import ProtectedSectionBaseFactory
from async_bittrex.groups.protected_group import protected_group_factory


account_factory = ProtectedSectionBaseFactory()





from .v1 import Account_v1_1

account_factory.register("v1.1", Account_v1_1, protected_group_factory.get_version("v1.1"))


