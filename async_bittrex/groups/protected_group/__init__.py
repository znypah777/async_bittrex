

from async_bittrex.bases.factory import ProtectedSectionBaseFactory

protected_group_factory = ProtectedSectionBaseFactory()

from .v1 import ProtectedGroup_v1_1


protected_group_factory.register("v1.1", ProtectedGroup_v1_1)
