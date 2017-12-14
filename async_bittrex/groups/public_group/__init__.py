
<<<<<<< HEAD
from async_bittrex.bases.factory import AccessLevelGroupFactory
from async_bittrex.groups.base_group import internalgroup_factory


public_group_factory = AccessLevelGroupFactory()

from .v1 import PublicGroup_v1_1

public_group_factory.register("v1.1", PublicGroup_v1_1, internalgroup_factory.get_version("v1.1"))
public_group_factory.register("v2.0", PublicGroup_v1_1, internalgroup_factory.get_version("v2.0"))
=======
from async_bittrex.bases.factory import PublicSectionBaseFactory
from async_bittrex.groups.base_group import basegroup_factory


public_group_factory = PublicSectionBaseFactory()

from .v1 import PublicGroup_v1_1
public_group_factory.register("v1.1", PublicGroup_v1_1, basegroup_factory.get_version("v1.1"))
>>>>>>> 2848be7fbd43c38bbf7a58905e918fd5508c0b4b
