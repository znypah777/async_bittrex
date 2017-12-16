from async_bittrex.bases.factory import AccessLevelGroupFactory
from async_bittrex.groups.base_group import internalgroup_factory


public_group_factory = AccessLevelGroupFactory()

from .v1 import PublicGroup_v1_1

public_group_factory.register("v1.1", PublicGroup_v1_1, internalgroup_factory.get_version("v1.1"))
public_group_factory.register("v2.0", PublicGroup_v1_1, internalgroup_factory.get_version("v2.0"))
