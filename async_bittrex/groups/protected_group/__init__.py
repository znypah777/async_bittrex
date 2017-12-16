from async_bittrex.bases.factory import AccessLevelGroupFactory
from async_bittrex.groups.base_group import internalgroup_factory

protected_group_factory = AccessLevelGroupFactory()

from .v1 import ProtectedGroup_v1_1


protected_group_factory.register("v1.1", ProtectedGroup_v1_1, internalgroup_factory.get_version("v1.1"))

