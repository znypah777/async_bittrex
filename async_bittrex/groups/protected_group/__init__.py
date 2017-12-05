

from async_bittrex.bases.factory import ProtectedSectionBaseFactory
from async_bittrex.groups.base_group import basegroup_factory

protected_group_factory = ProtectedSectionBaseFactory()

from .v1 import ProtectedGroup_v1_1


protected_group_factory.register("v1.1", ProtectedGroup_v1_1, basegroup_factory.get_version("v1.1"))

