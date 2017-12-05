from async_bittrex.bases.factory import PublicSectionBaseFactory
from async_bittrex.groups.public_group import public_group_factory



public_factory = PublicSectionBaseFactory()




from .v1 import Public_v1_1

public_factory.register("v1.1", Public_v1_1, public_group_factory.get_version("v1.1"))