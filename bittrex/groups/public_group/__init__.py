
from bittrex.bases.factory import PublicSectionBaseFactory

public_group_factory = PublicSectionBaseFactory()

from .v1 import PublicGroup_v1_1
public_group_factory.register("v1.1", PublicGroup_v1_1)