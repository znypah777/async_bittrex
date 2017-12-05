
from async_bittrex.bases.factory import PublicSectionBaseFactory
from async_bittrex.groups.base_group import basegroup_factory


public_group_factory = PublicSectionBaseFactory()

from .v1 import PublicGroup_v1_1
public_group_factory.register("v1.1", PublicGroup_v1_1, basegroup_factory.get_version("v1.1"))