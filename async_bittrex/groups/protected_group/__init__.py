

<<<<<<< HEAD
from async_bittrex.bases.factory import AccessLevelGroupFactory
from async_bittrex.groups.base_group import internalgroup_factory

protected_group_factory = AccessLevelGroupFactory()
=======
from async_bittrex.bases.factory import ProtectedSectionBaseFactory
from async_bittrex.groups.base_group import basegroup_factory

protected_group_factory = ProtectedSectionBaseFactory()
>>>>>>> 2848be7fbd43c38bbf7a58905e918fd5508c0b4b

from .v1 import ProtectedGroup_v1_1


<<<<<<< HEAD
protected_group_factory.register("v1.1", ProtectedGroup_v1_1, internalgroup_factory.get_version("v1.1"))
=======
protected_group_factory.register("v1.1", ProtectedGroup_v1_1, basegroup_factory.get_version("v1.1"))
>>>>>>> 2848be7fbd43c38bbf7a58905e918fd5508c0b4b

